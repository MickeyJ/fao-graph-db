# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for emissions_agriculture_energy UTILIZES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EmissionsAgricultureEnergyUtilizesMigrator(GraphMigrationBase):
    """Migrator for emissions_agriculture_energy UTILIZES relationships"""
    
    def __init__(self):
        super().__init__("emissions_agriculture_energy", "relationship")
        self.relationship_type = "UTILIZES"
        
        self.element_codes = ['72184']
        
        self.relationship_properties = {"element": "Energy use in agriculture", "element_code": "72184", "element_codes": ["72184"]}
    
    def get_migration_query(self) -> str:
        return load_sql("emissions_agriculture_energy_utilizes.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("emissions_agriculture_energy_utilizes_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("emissions_agriculture_energy_utilizes_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for emissions_agriculture_energy UTILIZES relationships"""
        logger.info(f"Starting emissions_agriculture_energy UTILIZES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 72184")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['72184'], 'element': 'Energy use in agriculture', 'element_code': '72184'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} UTILIZES relationships from emissions_agriculture_energy")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nemissions_agriculture_energy relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate emissions_agriculture_energy relationships: {e}")
            raise MigrationError(f"emissions_agriculture_energy relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass