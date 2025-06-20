# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for development_assistance_to_agriculture SHARES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class DevelopmentAssistanceToAgricultureSharesMigrator(GraphMigrationBase):
    """Migrator for development_assistance_to_agriculture SHARES relationships"""
    
    def __init__(self):
        super().__init__("development_assistance_to_agriculture", "relationship")
        self.relationship_type = "SHARES"
        
        
        self.relationship_properties = {"pattern": "donor_recipient", "source_fk": "recipient_country_code_id", "target_fk": "donor_id"}
    
    def get_migration_query(self) -> str:
        return load_sql("development_assistance_to_agriculture_shares.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("development_assistance_to_agriculture_shares_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("development_assistance_to_agriculture_shares_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for development_assistance_to_agriculture SHARES relationships"""
        logger.info(f"Starting development_assistance_to_agriculture SHARES relationship migration...")
        
        
        logger.info(f"  Relationship type properties: {'pattern': 'donor_recipient', 'source_fk': 'recipient_country_code_id', 'target_fk': 'donor_id'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} SHARES relationships from development_assistance_to_agriculture")
            
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