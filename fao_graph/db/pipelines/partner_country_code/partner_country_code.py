# yaml_migrator.py.jinja2
# Generated migrator for node partner_country_code
import json
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class PartnerCountryCodeMigrator(GraphMigrationBase):
    """Migrator for PartnerCountryCode nodes from partner_country_codes"""
    
    def __init__(self):
        super().__init__(
            "partner_country_codes", 
            "node", 
            "fao_graph", 
            "PartnerCountryCode", 
        )
    
    def get_migration_query(self) -> str:
        return load_sql("partner_country_code.cypher.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("partner_country_code_verify.cypher.sql", Path(__file__).parent)

    def get_index_queries(self) -> str:
        return load_sql("partner_country_code_indexes.sql", Path(__file__).parent)

    def create(self, records, session):
        """Create nodes in AGE"""

        logger.info(f"Creating PartnerCountryCode nodes")

        # session.execute(text("SELECT create_vlabel('fao_graph', 'PartnerCountryCode');"))

        for record in records:
            # Build properties string
            props_parts = []

            # Always include id first
            props_parts.append(f"id: {record.id}")
            
            if hasattr(record, "partner_country_code") and getattr(record, "partner_country_code") is not None:
                value = getattr(record, "partner_country_code")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    value = value.replace("'", "\\'")
                    props_parts.append(f"partner_country_code: '{value}'")
                else:
                    props_parts.append(f"partner_country_code: {value}")
            if hasattr(record, "partner_countries") and getattr(record, "partner_countries") is not None:
                value = getattr(record, "partner_countries")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    value = value.replace("'", "\\'")
                    props_parts.append(f"partner_countries: '{value}'")
                else:
                    props_parts.append(f"partner_countries: {value}")
            if hasattr(record, "partner_country_code_m49") and getattr(record, "partner_country_code_m49") is not None:
                value = getattr(record, "partner_country_code_m49")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    value = value.replace("'", "\\'")
                    props_parts.append(f"partner_country_code_m49: '{value}'")
                else:
                    props_parts.append(f"partner_country_code_m49: {value}")
            if hasattr(record, "source_dataset") and getattr(record, "source_dataset") is not None:
                value = getattr(record, "source_dataset")
                
                if isinstance(value, str):
                    # Escape single quotes for Cypher
                    value = value.replace("'", "\\'")
                    props_parts.append(f"source_dataset: '{value}'")
                else:
                    props_parts.append(f"source_dataset: {value}")
            
            props_str = ", ".join(props_parts)
            
            # Build query without parameters - use string concatenation for braces
            query = text(f"""
                SELECT * FROM cypher('fao_graph', $$
                    CREATE (n:PartnerCountryCode """ + "{" + props_str + "}" + f""")
                    RETURN n
                $$) AS (result agtype)
            """)
            
            # Log every 500 records
            if self.created % 500 == 0:
                print("{" + props_str + "}")

            session.execute(query)
            self.created += 1
        
