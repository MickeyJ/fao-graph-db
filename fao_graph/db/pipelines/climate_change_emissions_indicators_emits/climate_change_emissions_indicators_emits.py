# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for climate_change_emissions_indicators EMITS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ClimateChangeEmissionsIndicatorsEmitsMigrator(GraphMigrationBase):
    """Migrator for climate_change_emissions_indicators EMITS relationships"""
    
    def __init__(self):
        super().__init__("climate_change_emissions_indicators", "relationship")
        self.relationship_type = "EMITS"
        self.element_codes = ['7179', '726313', '7264', '7265', '7266', '7279', '72791', '72792']
        self.elements = ['Emissions Share (CO2eq) (AR5) (F-gases)', 'Emissions Share (CO2eq) (AR5)', 'Emissions Share (CO2)', 'Emissions Share (CH4)', 'Emissions Share (N2O)', 'Emissions per capita', 'Emissions per value of agricultural production', 'Emissions per area of agricultural land']
        self.relationship_properties = {"category": "general", "element": "Emissions per area of agricultural land", "element_code": "72792", "gas_type": "unspecified", "source": "other"}
    
    def get_migration_query(self) -> str:
        return load_sql("climate_change_emissions_indicators_emits.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("climate_change_emissions_indicators_emits_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("climate_change_emissions_indicators_emits_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for climate_change_emissions_indicators EMITS relationships"""
        logger.info(f"Starting climate_change_emissions_indicators EMITS relationship migration...")
        logger.info(f"  Elements: Emissions Share (CO2eq) (AR5) (F-gases), Emissions Share (CO2eq) (AR5), Emissions Share (CO2), Emissions Share (CH4), Emissions Share (N2O), Emissions per capita, Emissions per value of agricultural production, Emissions per area of agricultural land")
        logger.info(f"  Properties: {'source': 'other', 'gas_type': 'unspecified', 'category': 'general', 'element_code': '72792', 'element': 'Emissions per area of agricultural land'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMITS relationships from climate_change_emissions_indicators")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nclimate_change_emissions_indicators relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate climate_change_emissions_indicators relationships: {e}")
            raise MigrationError(f"climate_change_emissions_indicators relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass