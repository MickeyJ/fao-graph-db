# yaml_migrator.py.jinja2
# Generated migrator for relationship prices__has_price
import json
from pathlib import Path
from sqlalchemy import text
from fao_graph.core.exceptions import MigrationError
from fao_graph.db.database import get_session
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class PricesHasPriceMigrator(GraphMigrationBase):
    """Migrator for HAS_PRICE relationships from prices"""
    
    def __init__(self):
        super().__init__("prices", "relationship", "fao_graph", "")
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
                AND t.year >= 2020
                AND elements.element_code IN ('5530', '5532')
                AND flags.flag IN ('A', 'X')
        """
    
    def create(self, records, session):
        """Create relationships in AGE"""

        try:
            for record in records:
                # Get source and target ids
                source_id = getattr(record, "area_code_id")
                target_id = getattr(record, "item_code_id")

                # Log every 500 records
                if self.created % 500 == 0:
                    logger.info(f"prices - (area_code_id: {source_id})-[:HAS_PRICE]->(item_code_id: {target_id})")
                
                # Build relationship properties string
                props_parts = []
                
                if hasattr(record, "year") and getattr(record, "year") is not None:
                    value = getattr(record, "year")
                    if isinstance(value, str):
                        value = value.replace("'", "\\'")
                        props_parts.append(f'year: "{value}"')
                        # props_parts.append(f"year: '{value}'")
                    else:
                        props_parts.append(f"year: {value}")
                if hasattr(record, "months") and getattr(record, "months") is not None:
                    value = getattr(record, "months")
                    if isinstance(value, str):
                        value = value.replace("'", "\\'")
                        props_parts.append(f'months: "{value}"')
                        # props_parts.append(f"months: '{value}'")
                    else:
                        props_parts.append(f"months: {value}")
                if hasattr(record, "value") and getattr(record, "value") is not None:
                    value = getattr(record, "value")
                    if isinstance(value, str):
                        value = value.replace("'", "\\'")
                        props_parts.append(f'value: "{value}"')
                        # props_parts.append(f"value: '{value}'")
                    else:
                        props_parts.append(f"value: {value}")
                if hasattr(record, "unit") and getattr(record, "unit") is not None:
                    value = getattr(record, "unit")
                    if isinstance(value, str):
                        value = value.replace("'", "\\'")
                        props_parts.append(f'unit: "{value}"')
                        # props_parts.append(f"unit: '{value}'")
                    else:
                        props_parts.append(f"unit: {value}")
                
                if hasattr(record, "element_code") and getattr(record, "element_code") is not None:
                    value = getattr(record, "element_code")
                    if isinstance(value, str):
                        value = value.replace("'", "\\'")
                        props_parts.append(f'element_code: "{value}"')
                        # props_parts.append(f"element_code: '{value}'")
                    else:
                        props_parts.append(f"element_code: {value}")
                        
                if hasattr(record, "element") and getattr(record, "element") is not None:
                    value = getattr(record, "element")
                    if isinstance(value, str):
                        value = value.replace("'", "\\'")
                        props_parts.append(f'element: "{value}"')
                        # props_parts.append(f"element: '{value}'")
                    else:
                        props_parts.append(f"element: {value}")
                if hasattr(record, "flag") and getattr(record, "flag") is not None:
                    value = getattr(record, "flag")
                    if isinstance(value, str):
                        value = value.replace("'", "\\'")
                        props_parts.append(f'flag: "{value}"')
                        # props_parts.append(f"flag: '{value}'")
                    else:
                        props_parts.append(f"flag: {value}")
                        
                if hasattr(record, "description") and getattr(record, "description") is not None:
                    value = getattr(record, "description")
                    if isinstance(value, str):
                        value = value.replace("'", "\\'")
                        props_parts.append(f'description: "{value}"')
                        # props_parts.append(f"description: '{value}'")
                    else:
                        props_parts.append(f"description: {value}")
                
                props_parts.append("source_dataset: 'prices'")
                props_str = ", ".join(props_parts)
                
                # Build query without parameters
                query = text(f"""
                    SELECT * FROM cypher('fao_graph', $$
                        MATCH (source:AreaCode """ + "{" + f"id: {source_id}, source_dataset: 'prices'" + "}" + f""")
                        MATCH (target:ItemCode """ + "{" + f"id: {target_id}, source_dataset: 'prices'" + "}" + f""")
                        CREATE (source)-[r:HAS_PRICE """ + "{" + props_str + "}" + f"""]->(target)
                        RETURN r
                    $$) AS (result agtype)
                """)
                
                session.execute(query)
                self.created += 1

            session.commit()
        except Exception as e:
            session.rollback()
            raise MigrationError(f"Failed to create relationships: {e}")
    
