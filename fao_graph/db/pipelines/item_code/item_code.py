# yaml_migrator.py.jinja2
# Generated migrator for node item_code
import json
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ItemCodeMigrator(GraphMigrationBase):
    """Migrator for ItemCode nodes from item_codes"""
    
    def __init__(self):
        super().__init__("item_codes", "node", "fao_graph", "ItemCode")
        self.node_label = "ItemCode"
    
    def get_migration_query(self) -> str:
        return load_sql("item_code.cypher.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("item_code_verify.cypher.sql", Path(__file__).parent)

    def get_index_queries(self) -> str:
        return load_sql("item_code_indexes.sql", Path(__file__).parent)

    def create(self, records, session):
        """Create nodes in AGE"""

        logger.info(f"Creating ItemCode nodes")

        for record in records:
            # Build properties string
            props_parts = []

            
            # Always include id first
            props_parts.append(f"id: {record.id}")
            
            if hasattr(record, "item_code") and getattr(record, "item_code") is not None:
                value = getattr(record, "item_code")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    # value = value.replace("'", "\\'")
                    props_parts.append(f'item_code: "{value}"')
                else:
                    props_parts.append(f"item_code: {value}")
            if hasattr(record, "item") and getattr(record, "item") is not None:
                value = getattr(record, "item")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    # value = value.replace("'", "\\'")
                    props_parts.append(f'item: "{value}"')
                else:
                    props_parts.append(f"item: {value}")
            if hasattr(record, "item_code_cpc") and getattr(record, "item_code_cpc") is not None:
                value = getattr(record, "item_code_cpc")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    # value = value.replace("'", "\\'")
                    props_parts.append(f'item_code_cpc: "{value}"')
                else:
                    props_parts.append(f"item_code_cpc: {value}")
            if hasattr(record, "item_code_fbs") and getattr(record, "item_code_fbs") is not None:
                value = getattr(record, "item_code_fbs")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    # value = value.replace("'", "\\'")
                    props_parts.append(f'item_code_fbs: "{value}"')
                else:
                    props_parts.append(f"item_code_fbs: {value}")
            if hasattr(record, "item_code_sdg") and getattr(record, "item_code_sdg") is not None:
                value = getattr(record, "item_code_sdg")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    # value = value.replace("'", "\\'")
                    props_parts.append(f'item_code_sdg: "{value}"')
                else:
                    props_parts.append(f"item_code_sdg: {value}")
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
                    CREATE (n:ItemCode """ + "{" + props_str + "}" + f""")
                    RETURN n
                $$) AS (result agtype)
            """)
            
            # Log every 500 records
            if self.created % 500 == 0:
                print("{" + props_str + "}")

            session.execute(query)
            self.created += 1
        
