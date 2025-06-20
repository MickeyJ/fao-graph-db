# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for inputs_land_use EMITS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class InputsLandUseEmitsMigrator(GraphMigrationBase):
    """Migrator for inputs_land_use EMITS relationships"""
    
    def __init__(self):
        super().__init__("inputs_land_use", "relationship")
        self.relationship_type = "EMITS"
        
        self.element_codes = ['72151']
        
        self.relationship_properties = {"element": "Carbon stock in living biomass", "element_code": "72151", "element_codes": ["72151"]}
    
    def get_migration_query(self) -> str:
        return load_sql("inputs_land_use_emits.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("inputs_land_use_emits_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("inputs_land_use_emits_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for inputs_land_use EMITS relationships"""
        logger.info(f"Starting inputs_land_use EMITS relationship migration...")
        
        logger.info(f"  Filtering on element codes: 72151")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['72151'], 'element': 'Carbon stock in living biomass', 'element_code': '72151'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMITS relationships from inputs_land_use")
            
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