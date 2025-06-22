# yaml_migrator.py.jinja2
# Generated migrator for relationship trade_detailed_trade_matrix__trades
import json
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class TradeDetailedTradeMatrixTradesMigrator(GraphMigrationBase):
    """Migrator for TRADES relationships from trade_detailed_trade_matrix"""
    
    def __init__(self):
        super().__init__("trade_detailed_trade_matrix", "relationship", "fao_graph", "")
        self.relationship_type = "TRADES"
    
    def get_migration_query(self) -> str:
        return load_sql("trade_detailed_trade_matrix__trades.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("trade_detailed_trade_matrix__trades_verify.cypher.sql", Path(__file__).parent)

    def get_count_query(self) -> str:
        """Count records matching our filters"""
        return f"""
            SELECT COUNT(*) as total
            FROM trade_detailed_trade_matrix t
            JOIN item_codes ON t.item_code_id = item_codes.id
            JOIN elements ON t.element_code_id = elements.id
            JOIN flags ON t.flag_id = flags.id
            WHERE t.reporter_country_code_id IS NOT NULL
                AND t.partner_country_code_id IS NOT NULL
                AND t.value > 0
                AND t.value != 'NaN'
                AND t.value IS NOT NULL
                AND t.year >= 2022
                AND elements.element_code IN ('5910', '5922', '5610', '5622')
                AND flags.flag IN ('A')
        """
    
    def create(self, records, session):
        """Create relationships in AGE"""

        for record in records:
            # Get source and target ids
            source_id = getattr(record, "reporter_country_code_id")
            target_id = getattr(record, "partner_country_code_id")

            # Log every 500 records
            if self.created % 500 == 0:
                logger.info(f"trade_detailed_trade_matrix - (reporter_country_code_id: {source_id})-[:TRADES]->(partner_country_code_id: {target_id})")
            
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
            
            if hasattr(record, "item_code") and getattr(record, "item_code") is not None:
                value = getattr(record, "item_code")
                if isinstance(value, str):
                    value = value.replace("'", "\\'")
                    props_parts.append(f'item_code: "{value}"')
                    # props_parts.append(f"item_code: '{value}'")
                else:
                    props_parts.append(f"item_code: {value}")
                    
            if hasattr(record, "item") and getattr(record, "item") is not None:
                value = getattr(record, "item")
                if isinstance(value, str):
                    value = value.replace("'", "\\'")
                    props_parts.append(f'item: "{value}"')
                    # props_parts.append(f"item: '{value}'")
                else:
                    props_parts.append(f"item: {value}")
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
            
            props_parts.append("source_dataset: 'trade_detailed_trade_matrix'")
            props_str = ", ".join(props_parts)
            
            # Build query without parameters
            query = text(f"""
                SELECT * FROM cypher('fao_graph', $$
                    MATCH (source:ReporterCountryCode """ + "{" + f"id: {source_id}, source_dataset: 'trade_detailed_trade_matrix'" + "}" + f""")
                    MATCH (target:PartnerCountryCode """ + "{" + f"id: {target_id}, source_dataset: 'trade_detailed_trade_matrix'" + "}" + f""")
                    CREATE (source)-[r:TRADES """ + "{" + props_str + "}" + f"""]->(target)
                    RETURN r
                $$) AS (result agtype)
            """)
            
            session.execute(query)
            self.created += 1
    
