# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for exchange_rate EXCHANGES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ExchangeRateExchangesMigrator(GraphMigrationBase):
    """Migrator for exchange_rate EXCHANGES relationships"""
    
    def __init__(self):
        super().__init__("exchange_rate", "relationship")
        self.relationship_type = "EXCHANGES"
    
    def get_migration_query(self) -> str:
        return load_sql("exchange_rate_exchanges.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("exchange_rate_exchanges_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("exchange_rate_exchanges_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for exchange_rate EXCHANGES relationships"""
        logger.info(f"Starting exchange_rate EXCHANGES relationship migration...")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EXCHANGES relationships from exchange_rate")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nexchange_rate relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate exchange_rate relationships: {e}")
            raise MigrationError(f"exchange_rate relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass