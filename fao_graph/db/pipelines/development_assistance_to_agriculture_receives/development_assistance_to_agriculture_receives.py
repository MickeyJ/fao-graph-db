# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for development_assistance_to_agriculture RECEIVES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class DevelopmentAssistanceToAgricultureReceivesMigrator(GraphMigrationBase):
    """Migrator for development_assistance_to_agriculture RECEIVES relationships"""
    
    def __init__(self):
        super().__init__("development_assistance_to_agriculture", "relationship")
        self.relationship_type = "RECEIVES"
    
    def get_migration_query(self) -> str:
        return load_sql("development_assistance_to_agriculture_receives.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("development_assistance_to_agriculture_receives_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("development_assistance_to_agriculture_receives_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for development_assistance_to_agriculture RECEIVES relationships"""
        logger.info(f"Starting development_assistance_to_agriculture RECEIVES relationship migration...")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} RECEIVES relationships from development_assistance_to_agriculture")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ndevelopment_assistance_to_agriculture relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate development_assistance_to_agriculture relationships: {e}")
            raise MigrationError(f"development_assistance_to_agriculture relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass