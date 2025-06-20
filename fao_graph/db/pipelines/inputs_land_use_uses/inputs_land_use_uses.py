# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for inputs_land_use USES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class InputsLandUseUsesMigrator(GraphMigrationBase):
    """Migrator for inputs_land_use USES relationships"""
    
    def __init__(self):
        super().__init__("inputs_land_use", "relationship")
        self.relationship_type = "USES"
        self.element_codes = ['5110', '7208', '7209', '7210', '72151', '7252', '7277', '7278']
        self.elements = ['Area', 'Share in Agricultural land', 'Share in Land area', 'Share in Forest land', 'Carbon stock in living biomass', 'Share in Cropland', 'Area per capita', 'Value of agricultural production (Int. $) per Area']
        self.relationship_properties = {"element": "Value of agricultural production (Int. $) per Area", "element_code": "7278", "measure": "value", "resource": "inputs"}
    
    def get_migration_query(self) -> str:
        return load_sql("inputs_land_use_uses.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("inputs_land_use_uses_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("inputs_land_use_uses_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for inputs_land_use USES relationships"""
        logger.info(f"Starting inputs_land_use USES relationship migration...")
        logger.info(f"  Elements: Area, Share in Agricultural land, Share in Land area, Share in Forest land, Carbon stock in living biomass, Share in Cropland, Area per capita, Value of agricultural production (Int. $) per Area")
        logger.info(f"  Properties: {'resource': 'inputs', 'measure': 'value', 'element_code': '7278', 'element': 'Value of agricultural production (Int. $) per Area'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} USES relationships from inputs_land_use")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ninputs_land_use relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate inputs_land_use relationships: {e}")
            raise MigrationError(f"inputs_land_use relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass