# yaml_migrator.py.jinja2
# Generated migrator for relationship food_security_data__measures
import json
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class FoodSecurityDataMeasuresMigrator(GraphMigrationBase):
    """Migrator for MEASURES relationships from food_security_data"""
    
    def __init__(self):
        super().__init__("food_security_data", "relationship", "fao_graph", "")
        self.relationship_type = "MEASURES"
    
    def get_migration_query(self) -> str:
        return load_sql("food_security_data__measures.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("food_security_data__measures_verify.cypher.sql", Path(__file__).parent)

    def get_count_query(self) -> str:
        """Count records matching our filters"""
        return f"""
            SELECT COUNT(*) as total
            FROM food_security_data t
            JOIN elements ON t.element_code_id = elements.id
            JOIN flags ON t.flag_id = flags.id
            WHERE t.area_code_id IS NOT NULL
                AND t.item_code_id IS NOT NULL
                AND t.value > 0
                AND t.value != 'NaN'
                AND t.value IS NOT NULL
                AND elements.element_code IN ('6123', '6128', '6126', '6125', '6132', '6121', '6173', '6124')
                AND flags.flag IN ('A', 'X', 'E')
        """
    
    def create(self, records, session):
        """Create relationships in AGE"""

        for record in records:
            # Get source and target ids
            source_id = getattr(record, "area_code_id")
            target_id = getattr(record, "item_code_id")

            # Log every 500 records
            if self.created % 500 == 0:
                logger.info(f"food_security_data - (area_code_id: {source_id})-[:MEASURES]->(item_code_id: {target_id})")
            
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
            if hasattr(record, "note") and getattr(record, "note") is not None:
                value = getattr(record, "note")
                if isinstance(value, str):
                    value = value.replace("'", "\\'")
                    props_parts.append(f'note: "{value}"')
                    # props_parts.append(f"note: '{value}'")
                else:
                    props_parts.append(f"note: {value}")
            
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
            
            props_parts.append("source_dataset: 'food_security_data'")
            props_str = ", ".join(props_parts)
            
            # Build query without parameters
            query = text(f"""
                SELECT * FROM cypher('fao_graph', $$
                    MATCH (source:AreaCode """ + "{" + f"id: {source_id}, source_dataset: 'food_security_data'" + "}" + f""")
                    MATCH (target:ItemCode """ + "{" + f"id: {target_id}, source_dataset: 'food_security_data'" + "}" + f""")
                    CREATE (source)-[r:MEASURES """ + "{" + props_str + "}" + f"""]->(target)
                    RETURN r
                $$) AS (result agtype)
            """)
            
            session.execute(query)
            self.created += 1
    
