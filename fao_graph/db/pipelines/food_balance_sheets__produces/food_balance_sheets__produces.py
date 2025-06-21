# yaml_migrator.py.jinja2
# Generated migrator for relationship food_balance_sheets__produces
from pathlib import Path
from sqlalchemy import text

from fao_graph.db.database import get_session
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class FoodBalanceSheetsProducesMigrator(GraphMigrationBase):
    """Migrator for PRODUCES relationships from food_balance_sheets"""
    
    def __init__(self):
        super().__init__("food_balance_sheets", "relationship")
        self.relationship_type = "PRODUCES"
    
    def get_migration_query(self) -> str:
        return load_sql("food_balance_sheets__produces.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("food_balance_sheets__produces_verify.cypher.sql", Path(__file__).parent)

    def get_count_query(self) -> str:
        """Count records matching our filters"""
        return f"""
            SELECT COUNT(*) as total
            FROM food_balance_sheets t
            JOIN elements ON t.element_code_id = elements.id
            JOIN flags ON t.flag_id = flags.id
            WHERE t.area_code_id IS NOT NULL
                AND t.item_code_id IS NOT NULL
                AND t.value > 0
                AND elements.element_code IN ('5511', '5301')
                AND flags.flag IN ('A', 'X', 'E')
        """
    
    def create(self, records):
        """Create relationships in AGE"""
        with get_session() as session:
            for record in records:
                query = text("""
                    SELECT * FROM cypher('fao_graph', $$
                        MATCH (source:AreaCode {id: $source_id, source_dataset: "food_balance_sheets" })
                        MATCH (target:ItemCode {id: $target_id, source_dataset: "food_balance_sheets" })
                        CREATE (source)-[r:PRODUCES $props]->(target)
                        RETURN r
                    $$, $params) AS (result agtype)
                """)
                
                props = {
                    "year": getattr(record, "year"),
                    "value": getattr(record, "value"),
                    "unit": getattr(record, "unit"),
                    "note": getattr(record, "note"),
                    "element_code": getattr(record, "element_code"),
                    "element": getattr(record, "element"),
                    "flag": getattr(record, "flag"),
                    "description": getattr(record, "description"),
                    "source_dataset": "food_balance_sheets"
                }
                
                params = {
                    "source_id": getattr(record, "area_code_id"),
                    "target_id": getattr(record, "item_code_id"),
                    "props": props
                }
                
                session.execute(query, {
                    "params": params
                })
                self.created += 1

