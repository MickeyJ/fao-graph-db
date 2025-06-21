# yaml_migrator.py.jinja2
# Generated migrator for relationship trade_detailed_trade_matrix__trades
from pathlib import Path
from sqlalchemy import text
from fao_graph.core.exceptions import MigrationError
from fao_graph.db.database import get_session
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class TradeDetailedTradeMatrixTradesMigrator(GraphMigrationBase):
    """Migrator for TRADES relationships from trade_detailed_trade_matrix"""
    
    def __init__(self):
        super().__init__("trade_detailed_trade_matrix", "relationship")
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
                AND elements.element_code IN ('5610', '5910', '5622', '5922')
                AND flags.flag IN ('A', 'X', 'E')
        """
    
    def create(self, records):
        """Create relationships in AGE"""
        with get_session() as session:

            try:
                    
                for record in records:
                    query = text("""
                        SELECT * FROM cypher('fao_graph', $$
                            MATCH (source:ReporterCountryCode {id: $source_id, source_dataset: "trade_detailed_trade_matrix" })
                            MATCH (target:PartnerCountryCode {id: $target_id, source_dataset: "trade_detailed_trade_matrix" })
                            CREATE (source)-[r:TRADES $props]->(target)
                            RETURN r
                        $$, $params) AS (result agtype)
                    """)
                    
                    props = {
                        "year": getattr(record, "year"),
                        "value": getattr(record, "value"),
                        "unit": getattr(record, "unit"),
                        "item_code": getattr(record, "item_code"),
                        "item": getattr(record, "item"),
                        "element_code": getattr(record, "element_code"),
                        "element": getattr(record, "element"),
                        "flag": getattr(record, "flag"),
                        "description": getattr(record, "description"),
                        "source_dataset": "trade_detailed_trade_matrix"
                    }
                    
                    params = {
                        "source_id": getattr(record, "reporter_country_code_id"),
                        "target_id": getattr(record, "partner_country_code_id"),
                        "props": props
                    }
                    
                    session.execute(query, {
                        "params": params
                    })
                    self.created += 1

                session.commit()
            except Exception as e:
                session.rollback()
                raise MigrationError(f"Failed to create relationships: {e}")
