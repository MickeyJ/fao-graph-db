# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for emissions_land_use_fires EMITS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EmissionsLandUseFiresEmitsMigrator(GraphMigrationBase):
    """Migrator for emissions_land_use_fires EMITS relationships"""
    
    def __init__(self):
        super().__init__("emissions_land_use_fires", "relationship")
        self.relationship_type = "EMITS"
        self.element_codes = ['7225', '7230', '7245', '7246', '7273']
        self.elements = ['Emissions (CH4)', 'Emissions (N2O)', 'Burning crop residues (Biomass burned, dry matter)', 'Burned Area', 'Emissions (CO2)']
        self.relationship_properties = {"category": "general", "element": "Emissions (CO2)", "element_code": "7273", "gas_type": "CO2", "source": "other"}
    
    def get_migration_query(self) -> str:
        return load_sql("emissions_land_use_fires_emits.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("emissions_land_use_fires_emits_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("emissions_land_use_fires_emits_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for emissions_land_use_fires EMITS relationships"""
        logger.info(f"Starting emissions_land_use_fires EMITS relationship migration...")
        logger.info(f"  Elements: Emissions (CH4), Emissions (N2O), Burning crop residues (Biomass burned, dry matter), Burned Area, Emissions (CO2)")
        logger.info(f"  Properties: {'source': 'other', 'gas_type': 'CO2', 'category': 'general', 'element_code': '7273', 'element': 'Emissions (CO2)'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMITS relationships from emissions_land_use_fires")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nemissions_land_use_fires relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate emissions_land_use_fires relationships: {e}")
            raise MigrationError(f"emissions_land_use_fires relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass