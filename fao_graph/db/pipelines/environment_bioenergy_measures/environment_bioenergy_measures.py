# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for environment_bioenergy MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EnvironmentBioenergyMeasuresMigrator(GraphMigrationBase):
    """Migrator for environment_bioenergy MEASURES relationships"""
    
    def __init__(self):
        super().__init__("environment_bioenergy", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5851', '5852']
        self.elements = ['Energy consumption', 'Energy production']
        self.relationship_properties = {"category": "general", "element": "Energy production", "element_code": "5852", "measure": "other"}
    
    def get_migration_query(self) -> str:
        return load_sql("environment_bioenergy_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("environment_bioenergy_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("environment_bioenergy_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for environment_bioenergy MEASURES relationships"""
        logger.info(f"Starting environment_bioenergy MEASURES relationship migration...")
        logger.info(f"  Elements: Energy consumption, Energy production")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'other', 'element_code': '5852', 'element': 'Energy production'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from environment_bioenergy")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nenvironment_bioenergy relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate environment_bioenergy relationships: {e}")
            raise MigrationError(f"environment_bioenergy relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass