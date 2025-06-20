# Generated graph migrator for currencies
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class CurrencyMigrator(GraphMigrationBase):
    """Migrator for currencies node"""
    
    def __init__(self):
        super().__init__("currencies", "node")
    
    def get_migration_query(self) -> str:
        return load_sql("currency.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("currency_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
      return load_sql("currency_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for currencies"""
        logger.info(f"Starting currencies migration...")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created}  {self.migration_type}")
            
            # Create indexes using the existing method
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ncurrencies migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate currencies: {e}")
            raise MigrationError(f"currencies migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass