# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for environment_livestock_manure MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EnvironmentLivestockManureMeasuresMigrator(GraphMigrationBase):
    """Migrator for environment_livestock_manure MEASURES relationships"""
    
    def __init__(self):
        super().__init__("environment_livestock_manure", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5111', '72380', '723801', '723802', '72381', '723811', '723812', '72386', '72538', '72539']
        self.elements = ['Stocks', 'Manure left on pasture (N content)', 'Manure left on pasture that volatilises (N content)', 'Manure left on pasture that leaches (N content)', 'Manure applied to soils (N content)', 'Manure applied to soils that volatilises (N content)', 'Manure applied to soils that leaches (N content)', 'Manure management (manure treated, N content)', 'Amount excreted in manure (N content)', 'Losses from manure treated (N content)']
        self.relationship_properties = {"category": "general", "element": "Losses from manure treated (N content)", "element_code": "72539", "measure": "content"}
    
    def get_migration_query(self) -> str:
        return load_sql("environment_livestock_manure_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("environment_livestock_manure_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("environment_livestock_manure_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for environment_livestock_manure MEASURES relationships"""
        logger.info(f"Starting environment_livestock_manure MEASURES relationship migration...")
        logger.info(f"  Elements: Stocks, Manure left on pasture (N content), Manure left on pasture that volatilises (N content), Manure left on pasture that leaches (N content), Manure applied to soils (N content), Manure applied to soils that volatilises (N content), Manure applied to soils that leaches (N content), Manure management (manure treated, N content), Amount excreted in manure (N content), Losses from manure treated (N content)")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'content', 'element_code': '72539', 'element': 'Losses from manure treated (N content)'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from environment_livestock_manure")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nenvironment_livestock_manure relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate environment_livestock_manure relationships: {e}")
            raise MigrationError(f"environment_livestock_manure relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass