# yaml_migrator.py.jinja2
# Generated migrator for relationship prices__has_price
from pathlib import Path
from sqlalchemy import text

from fao_graph.db.database import get_session
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class PricesHasPriceMigrator(GraphMigrationBase):
    """Migrator for HAS_PRICE relationships from prices"""
    
    def __init__(self):
        super().__init__("prices", "relationship")
        self.relationship_type = "HAS_PRICE"
    
    def get_migration_query(self) -> str:
        return load_sql("prices__has_price.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("prices__has_price_verify.cypher.sql", Path(__file__).parent)

    def get_count_query(self) -> str:
        """Count records matching our filters"""
        return f"""
            SELECT COUNT(*) as total
            FROM prices t
            JOIN elements ON t.element_code_id = elements.id
            JOIN flags ON t.flag_id = flags.id
            WHERE t.area_code_id IS NOT NULL
                AND t.item_code_id IS NOT NULL
                AND t.value > 0
                AND elements.element_code IN ('5530', '5532')
                AND flags.flag IN ('A', 'X')
        """
    
    def create(self, records):
        """Create relationships in AGE"""
        with get_session() as session:
            for record in records:
                query = text("""
                    SELECT * FROM cypher('fao_graph', $$
                        MATCH (source:AreaCode {id: $source_id, source_dataset: "prices" })
                        MATCH (target:ItemCode {id: $target_id, source_dataset: "prices" })
                        CREATE (source)-[r:HAS_PRICE $props]->(target)
                        RETURN r
                    $$, $params) AS (result agtype)
                """)
                
                props = {
                    "year": getattr(record, "year"),
                    "months": getattr(record, "months"),
                    "value": getattr(record, "value"),
                    "unit": getattr(record, "unit"),
                    "element_code": getattr(record, "element_code"),
                    "element": getattr(record, "element"),
                    "flag": getattr(record, "flag"),
                    "description": getattr(record, "description"),
                    "source_dataset": "prices"
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

