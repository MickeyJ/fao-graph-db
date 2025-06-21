# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for emissions_drained_organic_soils EMITS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EmissionsDrainedOrganicSoilsEmitsMigrator(GraphMigrationBase):
    """Migrator for emissions_drained_organic_soils EMITS relationships"""
    
    def __init__(self):
        super().__init__("emissions_drained_organic_soils", "relationship")
        self.relationship_type = "EMITS"
        
        self.element_codes = ['7230', '7273', '5026']
        
        self.relationship_properties = {"element": "Emissions (N2O)", "element_code": "7230", "element_codes": ["7230", "7273", "5026"], "elements": true, "gas_type": "N2O"}
    
    def get_migration_query(self) -> str:
        return load_sql("emissions_drained_organic_soils_emits.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("emissions_drained_organic_soils_emits_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("emissions_drained_organic_soils_emits_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for emissions_drained_organic_soils EMITS relationships"""
        logger.info(f"Starting emissions_drained_organic_soils EMITS relationship migration...")
        
        logger.info(f"  Filtering on element codes: 7230, 7273, 5026")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['7230', '7273', '5026'], 'element': 'Emissions (N2O)', 'element_code': '7230', 'elements': True, 'gas_type': 'N2O'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMITS relationships from emissions_drained_organic_soils")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nemissions_drained_organic_soils relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate emissions_drained_organic_soils relationships: {e}")
            raise MigrationError(f"emissions_drained_organic_soils relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass