# yaml_migrator.py.jinja2
# Generated migrator for node area_code
import json
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class AreaCodeMigrator(GraphMigrationBase):
    """Migrator for AreaCode nodes from area_codes"""
    
    def __init__(self):
        super().__init__("area_codes", "node", "fao_graph", "AreaCode")
        self.node_label = "AreaCode"
    
    def get_migration_query(self) -> str:
        return load_sql("area_code.cypher.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("area_code_verify.cypher.sql", Path(__file__).parent)

    def get_index_queries(self) -> str:
        return load_sql("area_code_indexes.sql", Path(__file__).parent)

    def create(self, records, session):
        """Create nodes in AGE"""

        logger.info(f"Creating AreaCode nodes")

        for record in records:
            # Build properties string
            props_parts = []

            
            # Always include id first
            props_parts.append(f"id: {record.id}")
            
            if hasattr(record, "area_code") and getattr(record, "area_code") is not None:
                value = getattr(record, "area_code")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    # value = value.replace("'", "\\'")
                    props_parts.append(f'area_code: "{value}"')
                else:
                    props_parts.append(f"area_code: {value}")
            if hasattr(record, "area") and getattr(record, "area") is not None:
                value = getattr(record, "area")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    # value = value.replace("'", "\\'")
                    props_parts.append(f'area: "{value}"')
                else:
                    props_parts.append(f"area: {value}")
            if hasattr(record, "area_code_m49") and getattr(record, "area_code_m49") is not None:
                value = getattr(record, "area_code_m49")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    # value = value.replace("'", "\\'")
                    props_parts.append(f'area_code_m49: "{value}"')
                else:
                    props_parts.append(f"area_code_m49: {value}")
            if hasattr(record, "source_dataset") and getattr(record, "source_dataset") is not None:
                value = getattr(record, "source_dataset")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    # value = value.replace("'", "\\'")
                    props_parts.append(f'source_dataset: "{value}"')
                else:
                    props_parts.append(f"source_dataset: {value}")
            
            props_str = ", ".join(props_parts)
            
            # Build query without parameters - use string concatenation for braces
            query = text(f"""
                SELECT * FROM cypher('fao_graph', $$
                    CREATE (n:AreaCode """ + "{" + props_str + "}" + f""")
                    RETURN n
                $$) AS (result agtype)
            """)
            
            # Log every 500 records
            if self.created % 500 == 0:
                print("{" + props_str + "}")

            session.execute(query)
            self.created += 1
        
