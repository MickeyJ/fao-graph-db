# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for emissions_agriculture_energy EMITS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EmissionsAgricultureEnergyEmitsMigrator(GraphMigrationBase):
    """Migrator for emissions_agriculture_energy EMITS relationships"""
    
    def __init__(self):
        super().__init__("emissions_agriculture_energy", "relationship")
        self.relationship_type = "EMITS"
        
        self.element_codes = ['7225', '7230', '7273']
        
        self.relationship_properties = {"element": "Emissions (CH4)", "element_code": "7225", "element_codes": ["7225", "7230", "7273"], "elements": true, "gas_type": "CH4"}
    
    def get_migration_query(self) -> str:
        return load_sql("emissions_agriculture_energy_emits.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("emissions_agriculture_energy_emits_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("emissions_agriculture_energy_emits_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for emissions_agriculture_energy EMITS relationships"""
        logger.info(f"Starting emissions_agriculture_energy EMITS relationship migration...")
        
        logger.info(f"  Filtering on element codes: 7225, 7230, 7273")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['7225', '7230', '7273'], 'element': 'Emissions (CH4)', 'element_code': '7225', 'elements': True, 'gas_type': 'CH4'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMITS relationships from emissions_agriculture_energy")
            
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