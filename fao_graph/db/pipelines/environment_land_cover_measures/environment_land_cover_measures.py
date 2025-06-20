# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for environment_land_cover MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EnvironmentLandCoverMeasuresMigrator(GraphMigrationBase):
    """Migrator for environment_land_cover MEASURES relationships"""
    
    def __init__(self):
        super().__init__("environment_land_cover", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5006', '5007', '5008', '5013']
        self.elements = ['Area from CGLS', 'Area from MODIS', 'Area from CCI_LC', 'Area from WorldCover']
        self.relationship_properties = {"category": "general", "element": "Area from WorldCover", "element_code": "5013", "measure": "area"}
    
    def get_migration_query(self) -> str:
        return load_sql("environment_land_cover_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("environment_land_cover_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("environment_land_cover_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for environment_land_cover MEASURES relationships"""
        logger.info(f"Starting environment_land_cover MEASURES relationship migration...")
        logger.info(f"  Elements: Area from CGLS, Area from MODIS, Area from CCI_LC, Area from WorldCover")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'area', 'element_code': '5013', 'element': 'Area from WorldCover'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from environment_land_cover")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nenvironment_land_cover relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate environment_land_cover relationships: {e}")
            raise MigrationError(f"environment_land_cover relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass