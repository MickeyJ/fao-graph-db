# Generated graph migrator for surveys
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class SurveyMigrator(GraphMigrationBase):
    """Migrator for surveys node"""
    
    def __init__(self):
        super().__init__("surveys", "node")
    
    def get_migration_query(self) -> str:
        return load_sql("survey.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("survey_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
      return load_sql("survey_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for surveys"""
        logger.info(f"Starting surveys migration...")
        
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
            logger.warning(f"\nsurveys migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate surveys: {e}")
            raise MigrationError(f"surveys migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass