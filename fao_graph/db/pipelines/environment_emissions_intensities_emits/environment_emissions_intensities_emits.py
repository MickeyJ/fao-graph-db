# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for environment_emissions_intensities EMITS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EnvironmentEmissionsIntensitiesEmitsMigrator(GraphMigrationBase):
    """Migrator for environment_emissions_intensities EMITS relationships"""
    
    def __init__(self):
        super().__init__("environment_emissions_intensities", "relationship")
        self.relationship_type = "EMITS"
        
        self.element_codes = ['723113', '71761']
        
        self.relationship_properties = {"element": "Emissions (CO2eq) (AR5)", "element_code": "723113", "element_codes": ["723113", "71761"], "gas_type": "CO2"}
    
    def get_migration_query(self) -> str:
        return load_sql("environment_emissions_intensities_emits.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("environment_emissions_intensities_emits_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("environment_emissions_intensities_emits_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for environment_emissions_intensities EMITS relationships"""
        logger.info(f"Starting environment_emissions_intensities EMITS relationship migration...")
        
        logger.info(f"  Filtering on element codes: 723113, 71761")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['723113', '71761'], 'element': 'Emissions (CO2eq) (AR5)', 'element_code': '723113', 'gas_type': 'CO2'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMITS relationships from environment_emissions_intensities")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nenvironment_emissions_intensities relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate environment_emissions_intensities relationships: {e}")
            raise MigrationError(f"environment_emissions_intensities relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass