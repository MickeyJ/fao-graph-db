import argparse
from typing import Dict, Sequence
from sqlalchemy.engine import Row

from src.core import db_connections
from utils import logger
from .migrate_base import BaseMigrator


class PricesMigrator(BaseMigrator):
    """Migrate prices data to Neo4j relationships."""

    def __init__(self):
        super().__init__("prices")

    @classmethod
    def get_description(cls) -> str:
        return "Migrate price data to Neo4j (monthly and annual prices)"

    @classmethod
    def add_custom_arguments(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--create-indexes",
            action="store_true",
            help="create relationship indexes for production_crops_livestock data",
        )

    @classmethod
    def handle_custom_arguments(cls, migrator: BaseMigrator, args: argparse.Namespace) -> bool:
        if args.create_indexes:
            if isinstance(migrator, PricesMigrator):
                migrator.create_indexes()
                return True  # Skip normal migration
        return False

    def get_index_queries(self) -> list[str]:
        """Get index creation queries."""
        return [
            "CREATE INDEX prices_year IF NOT EXISTS FOR ()-[r:HAS_PRICE]-() ON (r.year)",
            "CREATE INDEX prices_element IF NOT EXISTS FOR ()-[r:HAS_PRICE]-() ON (r.element_code_id)",
            "CREATE INDEX prices_year_element IF NOT EXISTS FOR ()-[r:HAS_PRICE]-() ON (r.year, r.element_code_id)",
            "CREATE INDEX prices_month IF NOT EXISTS FOR ()-[r:HAS_PRICE]-() ON (r.months_code)",
        ]

    def get_count_query(self) -> str:
        """Count total price records to migrate."""
        return f"""
            SELECT COUNT(*) as total
            FROM {self.source_dataset}
            WHERE value IS NOT NULL
        """

    def get_migration_query(self) -> str:
        """Get price records to migrate."""
        return f"""
            SELECT 
                p.area_code_id,
                p.item_code_id,
                p.element_code_id,
                p.flag_id,
                p.year,
                p.months_code,
                p.months,
                p.value,
                p.unit
            FROM {self.source_dataset} p
            WHERE p.value IS NOT NULL
            ORDER BY p.year, p.area_code_id, p.item_code_id, p.months_code, p.id
            LIMIT :limit OFFSET :offset
        """

    def create_relationships(self, records: Sequence[Row]) -> None:
        """Create HAS_PRICE relationships."""
        field_mapping = {
            "area_code_id": "area_code_id",
            "item_code_id": "item_code_id",
            "element_code_id": "element_code_id",
            "flag_id": "flag_id",
            "year": "year",
            "months_code": "months_code",
            "months": "months",
            "value": "value",
            "unit": "unit",
        }
        relationships = self.transform_records_for_neo4j(records, field_mapping)

        with db_connections.neo4j_session() as session:
            with session.begin_transaction() as tx:
                result = tx.run(
                    """
                    UNWIND $rels as rel
                    MATCH (c:Country {id: rel.area_code_id, source_dataset: $source_dataset})
                    MATCH (i:Item {id: rel.item_code_id, source_dataset: $source_dataset})
                    CREATE (c)-[p:HAS_PRICE {
                        year: rel.year,
                        months_code: rel.months_code,
                        months: rel.months,
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

    def get_verification_queries(self) -> Dict[str, str]:
        return {
            "total_count": """
                MATCH ()-[p:HAS_PRICE]->()
                RETURN count(p) as total_relationships
            """,
            "monthly_vs_annual": """
                MATCH ()-[p:HAS_PRICE]->()
                RETURN 
                    CASE 
                        WHEN p.months_code = '7021' THEN 'Annual'
                        ELSE 'Monthly'
                    END as price_type,
                    count(*) as count
            """,
            "sample_usa_wheat_2023": """
                MATCH (c:Country {area_code: '231', source_dataset: $source_dataset})-[p:HAS_PRICE]->(i:Item)
                WHERE i.name CONTAINS 'Wheat' AND p.year = 2023
                RETURN c.name, i.name, p.year, p.months, p.value, p.unit
                ORDER BY p.months_code
                LIMIT 13
            """,
            "price_coverage_by_year": """
                MATCH ()-[p:HAS_PRICE]->()
                RETURN p.year, count(*) as price_records
                ORDER BY p.year DESC
                LIMIT 10
            """,
        }


if __name__ == "__main__":
    PricesMigrator.main()
