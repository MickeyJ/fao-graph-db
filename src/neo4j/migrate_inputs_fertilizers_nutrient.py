from typing import Dict, Sequence
from sqlalchemy.engine import Row

from src.core import db_connections

from .migrate_base import BaseMigrator


class InputsFertilizersNutrientMigrator(BaseMigrator):
    """Migrate inputs_fertilizers_nutrient to Neo4j USES_NUTRIENT relationships."""

    def __init__(self):
        super().__init__("inputs_fertilizers_nutrient")

    @classmethod
    def get_description(cls) -> str:
        return "Migrate inputs_fertilizers_nutrient data to Neo4j"

    def get_migration_query(self) -> str:
        return """
            SELECT 
                ifn.area_code_id,
                ifn.item_code_id,
                ifn.element_code_id,
                ifn.flag_id,
                ifn.year,
                ifn.value,
                ifn.unit
            FROM inputs_fertilizers_nutrient ifn
            JOIN area_codes ac ON ac.id = ifn.area_code_id
            JOIN item_codes ic ON ic.id = ifn.item_code_id
            JOIN elements e ON e.id = ifn.element_code_id
            WHERE ifn.value > 0
            ORDER BY ifn.year, ifn.area_code_id, ifn.item_code_id, ifn.element_code_id, ifn.id
            LIMIT :limit OFFSET :offset
        """

    def create_relationships(self, records: Sequence[Row]) -> None:
        """Create USES_NUTRIENT relationships in Neo4j."""
        # Use helper method for transformation
        field_mapping = {
            "area_code_id": "area_code_id",
            "item_code_id": "item_code_id",
            "element_code_id": "element_code_id",
            "flag_id": "flag_id",
            "year": "year",
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
                    MATCH (n:Item {id: rel.item_code_id, source_dataset: $source_dataset})
                    CREATE (c)-[u:USES_NUTRIENT {
                        year: rel.year,
                        element_code_id: rel.element_code_id,
                        value: rel.value,
                        unit: rel.unit,
                        flag_id: rel.flag_id
                    }]->(n)
                    RETURN count(u) as processed
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
                MATCH ()-[u:USES_NUTRIENT]->()
                RETURN count(u) as total_relationships
            """,
            "duplicate_check": """
                MATCH (c:Country)-[u:USES_NUTRIENT]->(n:Item)
                WITH c, n, u.year as year, u.element_code_id as element, count(*) as rel_count
                WHERE rel_count > 1
                RETURN count(*) as duplicate_combinations
            """,
            "sample_usa_nitrogen": """
                MATCH (c:Country {area_code: '231', source_dataset: $source_dataset})-[u:USES_NUTRIENT]->(n:Item)
                WHERE n.name CONTAINS 'nitrogen'
                  AND u.year = 2020
                MATCH (e:Element {id: u.element_code_id})
                RETURN c.name, n.name, e.name, u.value, u.unit
                ORDER BY u.value DESC
                LIMIT 5
            """,
        }


if __name__ == "__main__":
    InputsFertilizersNutrientMigrator.main()
