# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for forestry MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ForestryMeasuresMigrator(GraphMigrationBase):
    """Migrator for forestry MEASURES relationships"""
    
    def __init__(self):
        super().__init__("forestry", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5510', '5516', '5610', '5616', '5622', '5910', '5916', '5922']
        self.elements = ['Production', 'Production', 'Import quantity', 'Import quantity', 'Import value', 'Export quantity', 'Export quantity', 'Export value']
        self.relationship_properties = {"category": "general", "element": "Export value", "element_code": "5922", "measure": "value"}
    
    def get_migration_query(self) -> str:
        return load_sql("forestry_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("forestry_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("forestry_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for forestry MEASURES relationships"""
        logger.info(f"Starting forestry MEASURES relationship migration...")
        logger.info(f"  Elements: Production, Production, Import quantity, Import quantity, Import value, Export quantity, Export quantity, Export value")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'value', 'element_code': '5922', 'element': 'Export value'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from forestry")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nforestry relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate forestry relationships: {e}")
            raise MigrationError(f"forestry relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass