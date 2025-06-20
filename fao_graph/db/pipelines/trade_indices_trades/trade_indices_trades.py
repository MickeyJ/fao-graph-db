# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for trade_indices TRADES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class TradeIndicesTradesMigrator(GraphMigrationBase):
    """Migrator for trade_indices TRADES relationships"""
    
    def __init__(self):
        super().__init__("trade_indices", "relationship")
        self.relationship_type = "TRADES"
        
        self.element_codes = ['462', '464', '465', '492', '494', '495', '64', '65', '94', '95']
        
        self.relationship_properties = {"element": "Import Value Index (2014-2016 = 100)", "element_code": "462", "element_codes": ["462", "464", "465", "492", "494", "495", "64", "65", "94", "95"], "flow_direction": "bidirectional"}
    
    def get_migration_query(self) -> str:
        return load_sql("trade_indices_trades.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("trade_indices_trades_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("trade_indices_trades_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for trade_indices TRADES relationships"""
        logger.info(f"Starting trade_indices TRADES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 462, 464, 465, 492, 494... (10 total)")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['462', '464', '465', '492', '494', '495', '64', '65', '94', '95'], 'element': 'Import Value Index (2014-2016 = 100)', 'element_code': '462', 'flow_direction': 'bidirectional'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} TRADES relationships from trade_indices")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ntrade_indices relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate trade_indices relationships: {e}")
            raise MigrationError(f"trade_indices relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass