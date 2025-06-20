# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for emissions_land_use_forests EMITS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EmissionsLandUseForestsEmitsMigrator(GraphMigrationBase):
    """Migrator for emissions_land_use_forests EMITS relationships"""
    
    def __init__(self):
        super().__init__("emissions_land_use_forests", "relationship")
        self.relationship_type = "EMITS"
        self.element_codes = ['5110', '72332']
        self.elements = ['Area', 'Net emissions/removals (CO2) (Forest land)']
        self.relationship_properties = {"category": "general", "element": "Net emissions/removals (CO2) (Forest land)", "element_code": "72332", "gas_type": "CO2", "source": "other"}
    
    def get_migration_query(self) -> str:
        return load_sql("emissions_land_use_forests_emits.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("emissions_land_use_forests_emits_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("emissions_land_use_forests_emits_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for emissions_land_use_forests EMITS relationships"""
        logger.info(f"Starting emissions_land_use_forests EMITS relationship migration...")
        logger.info(f"  Elements: Area, Net emissions/removals (CO2) (Forest land)")
        logger.info(f"  Properties: {'source': 'other', 'gas_type': 'CO2', 'category': 'general', 'element_code': '72332', 'element': 'Net emissions/removals (CO2) (Forest land)'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMITS relationships from emissions_land_use_forests")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nemissions_land_use_forests relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate emissions_land_use_forests relationships: {e}")
            raise MigrationError(f"emissions_land_use_forests relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass