# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for environment_livestock_patterns MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EnvironmentLivestockPatternsMeasuresMigrator(GraphMigrationBase):
    """Migrator for environment_livestock_patterns MEASURES relationships"""
    
    def __init__(self):
        super().__init__("environment_livestock_patterns", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5118', '7211', '7213']
        self.elements = ['Stocks', 'Share in total livestock', 'Livestock units per agricultural land area']
        self.relationship_properties = {"category": "general", "element": "Livestock units per agricultural land area", "element_code": "7213", "measure": "area"}
    
    def get_migration_query(self) -> str:
        return load_sql("environment_livestock_patterns_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("environment_livestock_patterns_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("environment_livestock_patterns_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for environment_livestock_patterns MEASURES relationships"""
        logger.info(f"Starting environment_livestock_patterns MEASURES relationship migration...")
        logger.info(f"  Elements: Stocks, Share in total livestock, Livestock units per agricultural land area")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'area', 'element_code': '7213', 'element': 'Livestock units per agricultural land area'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from environment_livestock_patterns")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nenvironment_livestock_patterns relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate environment_livestock_patterns relationships: {e}")
            raise MigrationError(f"environment_livestock_patterns relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass