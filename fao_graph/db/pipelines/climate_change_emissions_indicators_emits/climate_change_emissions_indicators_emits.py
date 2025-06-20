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
        self.element_codes = ['7231', '7230', '7229']
        self.elements = ['Emissions (CO2)', 'Emissions (N2O)', 'Emissions (CH4)']
    
    def get_migration_query(self) -> str:
        return load_sql("climate_change_emissions_indicators_emits.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("climate_change_emissions_indicators_emits_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("climate_change_emissions_indicators_emits_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for climate_change_emissions_indicators EMITS relationships"""
        logger.info(f"Starting climate_change_emissions_indicators EMITS relationship migration...")
        logger.info(f"  Elements: Emissions (CO2), Emissions (N2O), Emissions (CH4)")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                
                # Add source_table property for tracking
                query = query.replace(
                    "CREATE (source)-[r:EMITS {",
                    "CREATE (source)-[r:EMITS {source_dataset: 'climate_change_emissions_indicators', "
                )
                
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