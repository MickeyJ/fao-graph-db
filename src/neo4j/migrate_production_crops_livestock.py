import argparse
from typing import Sequence
from sqlalchemy.engine import Row
from sqlalchemy import text

from src.core import db_connections
from utils import logger


class ProductionCropsLivestockMigrator:
    """Migrate production_crops_livestock to Neo4j relationships."""

    def __init__(self):
        self.batch_size = 5000
        self.relationships_created = 0
        self.relationships_updated = 0
        self.source_dataset = "production_crops_livestock"

    def migrate(self, start_offset: int = 0) -> None:
        """Main migration entry point with resume capability."""
        logger.info(f"Starting {self.source_dataset} migration from offset {start_offset:,}...")
        logger.info(f"Using batch size: {self.batch_size}")  # Add this

        # Count ALL records
        count_query = text(
            """
            SELECT COUNT(*) as total
            FROM production_crops_livestock pcl
            WHERE pcl.value > 0
                AND pcl.value IS NOT NULL
                AND pcl.value != 'NaN'
        """
        )

        with db_connections.pg_session() as session:
            total_records = session.execute(count_query).scalar() or 0
            logger.info(f"Total production records to migrate: {total_records:,}")

            if start_offset > 0:
                logger.info(
                    f"Resuming from offset {start_offset:,} ({start_offset/total_records*100:.1f}% already done)"
                )

        # FIXED: Added more columns to ORDER BY for deterministic ordering
        query = text(
            """
            SELECT 
                pcl.area_code_id,
                pcl.item_code_id,
                pcl.element_code_id,
                pcl.flag_id,
                pcl.year,
                pcl.value,
                pcl.unit
            FROM production_crops_livestock pcl
            JOIN area_codes ac ON ac.id = pcl.area_code_id
            JOIN item_codes ic ON ic.id = pcl.item_code_id
            JOIN elements e ON e.id = pcl.element_code_id
            WHERE pcl.value > 0
                AND pcl.value IS NOT NULL
                AND pcl.value != 'NaN'
            ORDER BY pcl.year, pcl.area_code_id, pcl.item_code_id, pcl.element_code_id, pcl.id
            LIMIT :limit OFFSET :offset
        """
        )

        offset = start_offset

        while offset < total_records:
            with db_connections.pg_session() as pg_session:
                # Fetch batch
                result = pg_session.execute(
                    query,
                    {"limit": self.batch_size, "offset": offset},
                )
                records = result.fetchall()

                if not records:
                    break

                # Process batch with deduplication
                self._create_production_relationships(records)
                offset += len(records)

                # Enhanced progress logging
                pct_complete = offset / total_records * 100
                logger.info(
                    f"Progress: {offset:,}/{total_records:,} records ({pct_complete:.1f}%) | "
                    f"Created: {self.relationships_created:,} | Updated: {self.relationships_updated:,}"
                )

    def _create_production_relationships(self, records) -> None:
        """Create PRODUCES relationships with better batching."""

        # Transform ALL records at once
        relationships = []
        for record in records:
            relationships.append(
                {
                    "area_code_id": record.area_code_id,
                    "item_code_id": record.item_code_id,
                    "element_code_id": record.element_code_id,
                    "flag_id": record.flag_id,
                    "year": record.year,
                    "value": float(record.value),
                    "unit": record.unit,
                }
            )

        # Single transaction, single query for ALL records
        with db_connections.neo4j_session() as session:
            with session.begin_transaction() as tx:
                result = tx.run(
                    """
                    UNWIND $rels as rel
                    MATCH (c:Country {id: rel.area_code_id, source_dataset: $source_dataset})
                    MATCH (i:Item {id: rel.item_code_id, source_dataset: $source_dataset})
                    CREATE (c)-[p:PRODUCES {
                        year: rel.year,
                        element_code_id: rel.element_code_id,
                        value: rel.value,
                        unit: rel.unit,
                        flag_id: rel.flag_id
                    }]->(i)
                    RETURN count(p) as processed
                """,
                    rels=relationships,
                    source_dataset=self.source_dataset,
                )

                processed = result.single()["processed"]
                self.relationships_created += processed
                tx.commit()

    def verify_migration(self) -> None:
        """Verify the migration completed successfully."""
        with db_connections.neo4j_session() as session:
            # Total count
            result = session.run(
                """
                MATCH ()-[p:PRODUCES]->()
                RETURN count(p) as total_relationships
            """
            )

            total = result.single()["total_relationships"]
            logger.info(f"Verification complete: {total:,} PRODUCES relationships exist")

            # Check for duplicates
            result = session.run(
                """
                MATCH (c:Country)-[p:PRODUCES]->(i:Item)
                WITH c, i, p.year as year, p.element_code_id as element, count(*) as rel_count
                WHERE rel_count > 1
                RETURN count(*) as duplicate_combinations
                """
            )

            duplicates = result.single()["duplicate_combinations"]
            if duplicates > 0:
                logger.warning(f"Found {duplicates:,} duplicate relationship combinations")
            else:
                logger.info("No duplicate relationships found!")

            # Sample check - USA wheat production
            result = session.run(
                """
                MATCH (c:Country {area_code: '231', source_dataset: $source_dataset})-[p:PRODUCES]->(i:Item)
                WHERE i.item_code = '15'  // Wheat
                  AND p.year = 2022
                RETURN c.name, i.name, p.value, p.unit
                LIMIT 5
            """,
                source_dataset=self.source_dataset,
            )

            logger.info("Sample USA wheat production:")
            for record in result:
                logger.info(f"  {record['c.name']} -> {record['i.name']}: {record['p.value']} {record['p.unit']}")

    def cleanup_duplicates(self) -> None:
        """Optional: Remove existing duplicate relationships."""
        logger.info("Cleaning up duplicate relationships...")

        with db_connections.neo4j_session() as session:
            # Delete duplicates keeping the one with lowest internal ID
            result = session.run(
                """
                MATCH (c:Country)-[p:PRODUCES]->(i:Item)
                WITH c, i, p.year as year, p.element_code_id as element, 
                     collect(p) as rels, count(*) as rel_count
                WHERE rel_count > 1
                UNWIND rels[1..] as duplicate_rel
                DELETE duplicate_rel
                RETURN count(*) as deleted
                """
            )

            deleted = result.single()["deleted"]
            logger.info(f"Deleted {deleted:,} duplicate relationships")


def main():
    """Run the production migration with command-line options."""
    parser = argparse.ArgumentParser(description="Migrate production data to Neo4j")
    parser.add_argument("--offset", type=int, default=0, help="Starting offset for resuming migration")
    parser.add_argument("--batch-size", type=int, default=5000, help="Batch size for processing")
    parser.add_argument(
        "--cleanup-duplicates", action="store_true", help="Clean up existing duplicates before migration"
    )
    args = parser.parse_args()

    migrator = ProductionCropsLivestockMigrator()
    migrator.batch_size = args.batch_size

    try:
        if args.cleanup_duplicates:
            migrator.cleanup_duplicates()
        else:
            migrator.migrate(start_offset=args.offset)
            migrator.verify_migration()

            logger.info(
                f"Migration complete! Created {migrator.relationships_created:,} new relationships, "
                f"updated {migrator.relationships_updated:,} existing ones"
            )

    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    main()
