# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for fertilizers_detailed_trade_matrix TRADES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class FertilizersDetailedTradeMatrixTradesMigrator(GraphMigrationBase):
    """Migrator for fertilizers_detailed_trade_matrix TRADES relationships"""
    
    def __init__(self):
        super().__init__("fertilizers_detailed_trade_matrix", "relationship")
        self.relationship_type = "TRADES"
    
    def get_migration_query(self) -> str:
        return load_sql("fertilizers_detailed_trade_matrix_trades.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("fertilizers_detailed_trade_matrix_trades_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("fertilizers_detailed_trade_matrix_trades_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for fertilizers_detailed_trade_matrix TRADES relationships"""
        logger.info(f"Starting fertilizers_detailed_trade_matrix TRADES relationship migration...")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} TRADES relationships from fertilizers_detailed_trade_matrix")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nfertilizers_detailed_trade_matrix relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate fertilizers_detailed_trade_matrix relationships: {e}")
            raise MigrationError(f"fertilizers_detailed_trade_matrix relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass