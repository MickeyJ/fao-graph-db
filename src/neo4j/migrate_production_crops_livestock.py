import argparse
from typing import Dict, Sequence
from sqlalchemy.engine import Row

from src.core import db_connections
from utils import logger
from .migrate_base import BaseMigrator


class ProductionCropsLivestockMigrator(BaseMigrator):
    """Migrate production_crops_livestock to Neo4j relationships."""

    def __init__(self):
        super().__init__("production_crops_livestock")

    @classmethod
    def get_description(cls) -> str:
        return "Migrate production data to Neo4j"

    @classmethod
    def add_custom_arguments(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--cleanup-duplicates", action="store_true", help="Clean up existing duplicates before migration"
        )

    @classmethod
    def handle_custom_arguments(cls, migrator: BaseMigrator, args: argparse.Namespace) -> bool:
        if args.cleanup_duplicates:
            if isinstance(migrator, ProductionCropsLivestockMigrator):
                migrator.cleanup_duplicates()
                return True  # Skip normal migration
        return False

    def get_count_query(self) -> str:
        """Override to count only records with notes for update mode."""
        # Check if we're in update mode by looking at sys.argv (bit hacky but works)
        import sys

        if "--mode" in sys.argv and "update" in sys.argv:
            return f"""
                SELECT COUNT(*) as total
                FROM {self.source_dataset} sds
                WHERE sds.value > 0
                  AND sds.note IS NOT NULL 
                  AND sds.note != ''
            """
        return super().get_count_query()

    def get_migration_query(self) -> str:
        # For updates, we only need records with notes
        import sys

        if "--mode" in sys.argv and "update" in sys.argv:
            return """
                SELECT 
                    pcl.area_code_id,
                    pcl.item_code_id,
                    pcl.element_code_id,
                    pcl.year,
                    pcl.note
                FROM production_crops_livestock pcl
                WHERE pcl.value > 0
                  AND pcl.note IS NOT NULL 
                  AND pcl.note != ''
                ORDER BY pcl.year, pcl.area_code_id, pcl.item_code_id, pcl.element_code_id, pcl.id
                LIMIT :limit OFFSET :offset
            """
        else:
            return """
                SELECT 
                    pcl.area_code_id,
                    pcl.item_code_id,
                    pcl.element_code_id,
                    pcl.flag_id,
                    pcl.year,
                    pcl.value,
                    pcl.unit,
                    pcl.note
                FROM production_crops_livestock pcl
                JOIN area_codes ac ON ac.id = pcl.area_code_id
                JOIN item_codes ic ON ic.id = pcl.item_code_id
                JOIN elements e ON e.id = pcl.element_code_id
                WHERE pcl.value > 0
                ORDER BY pcl.year, pcl.area_code_id, pcl.item_code_id, pcl.element_code_id, pcl.id
                LIMIT :limit OFFSET :offset
            """

    def create_relationships(self, records: Sequence[Row]) -> None:
        """Create PRODUCES relationships with better batching."""
        # Use helper method for transformation
        field_mapping = {
            "area_code_id": "area_code_id",
            "item_code_id": "item_code_id",
            "element_code_id": "element_code_id",
            "flag_id": "flag_id",
            "year": "year",
            "value": "value",
            "unit": "unit",
            "note": "note",
        }
        relationships = self.transform_records_for_neo4j(records, field_mapping)

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
                        note: rel.note,
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

    def update_relationships(self, records: Sequence[Row]) -> None:
        """Update existing PRODUCES relationships with notes."""
        updates = []
        for record in records:
            updates.append(
                {
                    "area_code_id": record.area_code_id,
                    "item_code_id": record.item_code_id,
                    "element_code_id": record.element_code_id,
                    "year": record.year,
                    "note": record.note,
                }
            )

        with db_connections.neo4j_session() as session:
            with session.begin_transaction() as tx:
                result = tx.run(
                    """
                    UNWIND $updates as upd
                    MATCH (c:Country {id: upd.area_code_id, source_dataset: $source_dataset})
                          -[p:PRODUCES {
                              year: upd.year,
                              element_code_id: upd.element_code_id
                          }]->
                          (i:Item {id: upd.item_code_id, source_dataset: $source_dataset})
                    SET p.note = upd.note
                    RETURN count(p) as updated
                    """,
                    updates=updates,
                    source_dataset=self.source_dataset,
                )

                updated = result.single()["updated"]
                self.relationships_updated += updated
                tx.commit()

    def get_verification_queries(self) -> Dict[str, str]:
        return {
            "total_count": """
                MATCH ()-[p:PRODUCES]->()
                RETURN count(p) as total_relationships
            """,
            "duplicate_check": """
                MATCH (c:Country)-[p:PRODUCES]->(i:Item)
                WITH c, i, p.year as year, p.element_code_id as element, count(*) as rel_count
                WHERE rel_count > 1
                RETURN count(*) as duplicate_combinations
            """,
            "sample_usa_wheat": """
                MATCH (c:Country {area_code: '231', source_dataset: $source_dataset})-[p:PRODUCES]->(i:Item)
                WHERE i.item_code = '15'  // Wheat
                  AND p.year = 2022
                RETURN c.name, i.name, p.value, p.unit
                LIMIT 5
            """,
        }

    def cleanup_duplicates(self) -> None:
        """Optional: Remove existing duplicate relationships."""
        logger.info("Cleaning up duplicate relationships...")

        with db_connections.neo4j_session() as session:
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


if __name__ == "__main__":
    ProductionCropsLivestockMigrator.main()
