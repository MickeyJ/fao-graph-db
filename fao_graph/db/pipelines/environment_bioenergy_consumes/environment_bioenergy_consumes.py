# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for environment_bioenergy CONSUMES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EnvironmentBioenergyConsumesMigrator(GraphMigrationBase):
    """Migrator for environment_bioenergy CONSUMES relationships"""
    
    def __init__(self):
        super().__init__("environment_bioenergy", "relationship")
        self.relationship_type = "CONSUMES"
        
        self.element_codes = ['5851']
        
        self.relationship_properties = {"element": "Energy consumption", "element_code": "5851", "element_codes": ["5851"], "elements": true}
    
    def get_migration_query(self) -> str:
        return load_sql("environment_bioenergy_consumes.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("environment_bioenergy_consumes_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("environment_bioenergy_consumes_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for environment_bioenergy CONSUMES relationships"""
        logger.info(f"Starting environment_bioenergy CONSUMES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 5851")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['5851'], 'element': 'Energy consumption', 'element_code': '5851', 'elements': True}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} CONSUMES relationships from environment_bioenergy")
            
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