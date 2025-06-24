# yaml_migrator.py.jinja2
# Generated migrator for relationship production_crops_livestock__produces
import json
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ProductionCropsLivestockProducesMigrator(GraphMigrationBase):
    """Migrator for PRODUCES relationships from production_crops_livestock"""
    
    def __init__(self):
        super().__init__(
            "production_crops_livestock", 
            "relationship", 
            "fao_graph", 
            "", 
            "PRODUCES",
            10000,
        )
    
    def get_migration_query(self) -> str:
        return load_sql("production_crops_livestock__produces.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("production_crops_livestock__produces_verify.cypher.sql", Path(__file__).parent)

    def get_total_rows_query(self) -> str:
        """Count records matching our filters"""
        return load_sql("production_crops_livestock__produces_total_rows.sql", Path(__file__).parent)
    
    def create(self, records, session):
        """Create relationships in AGE"""
        logger.warning(f"create() called with {len(records)} records")

        for record in records:
            # Get source and target ids
            source_id = getattr(record, "area_code_id")
            target_id = getattr(record, "item_code_id")

            # Log every 500 records
            if self.created % 500 == 0:
                logger.info(f"production_crops_livestock - (area_code_id: {source_id})-[:PRODUCES]->(item_code_id: {target_id})")
            
            # Build relationship properties string
            props_parts = []
            

            # Dataset Table Column
            if hasattr(record, "year") and getattr(record, "year") is not None:
                value = getattr(record, "year")
                if isinstance(value, str):
                    value = value.replace("'", "\\'")
                    props_parts.append(f"year: '{value}'")
                else:
                    props_parts.append(f"year: {value}")

            # Dataset Table Column
            if hasattr(record, "unit") and getattr(record, "unit") is not None:
                value = getattr(record, "unit")
                if isinstance(value, str):
                    value = value.replace("'", "\\'")
                    props_parts.append(f"unit: '{value}'")
                else:
                    props_parts.append(f"unit: {value}")

            # Dataset Table Column
            if hasattr(record, "value") and getattr(record, "value") is not None:
                value = getattr(record, "value")
                if isinstance(value, str):
                    value = value.replace("'", "\\'")
                    props_parts.append(f"value: '{value}'")
                else:
                    props_parts.append(f"value: {value}")

            # Dataset Table Column
            if hasattr(record, "note") and getattr(record, "note") is not None:
                value = getattr(record, "note")
                if isinstance(value, str):
                    value = value.replace("'", "\\'")
                    props_parts.append(f"note: '{value}'")
                else:
                    props_parts.append(f"note: {value}")

            # Join Table Code Column
            if hasattr(record, "element_code") and getattr(record, "element_code") is not None:
                value = getattr(record, "element_code")
                if isinstance(value, str):
                    value = value.replace("'", "\\'")
                    props_parts.append(f"element_code: '{value}'")
                else:
                    props_parts.append(f"element_code: {value}")

            # Join Table Description Column
            if hasattr(record, "element") and getattr(record, "element") is not None:
                value = getattr(record, "element")
                if isinstance(value, str):
                    value = value.replace("'", "\\'")
                    props_parts.append(f"element: '{value}'")
                else:
                    props_parts.append(f"element: {value}")

            # Join Table Code Column
            if hasattr(record, "flag") and getattr(record, "flag") is not None:
                value = getattr(record, "flag")
                if isinstance(value, str):
                    value = value.replace("'", "\\'")
                    props_parts.append(f"flag: '{value}'")
                else:
                    props_parts.append(f"flag: {value}")

            # Join Table Description Column
            if hasattr(record, "flag_description") and getattr(record, "flag_description") is not None:
                value = getattr(record, "flag_description")
                if isinstance(value, str):
                    value = value.replace("'", "\\'")
                    props_parts.append(f"flag_description: '{value}'")
                else:
                    props_parts.append(f"flag_description: {value}")
            
            props_parts.append("source_dataset: 'production_crops_livestock'")
            props_str = ", ".join(props_parts)
            
            # Build query without parameters
            query = text(f"""
                SELECT * FROM cypher('fao_graph', $$
                    MATCH (source:AreaCode """ + "{" + f"id: {source_id}, source_dataset: 'production_crops_livestock'" + "}" + f""")
                    MATCH (target:ItemCode """ + "{" + f"id: {target_id}, source_dataset: 'production_crops_livestock'" + "}" + f""")
                    CREATE (source)-[r:PRODUCES """ + "{" + props_str + "}" + f"""]->(target)
                    RETURN r
                $$) AS (result agtype)
            """)
            
            session.execute(query)
            self.created += 1

        logger.warning(f"create() completed, self.created now = {self.created}")
    
