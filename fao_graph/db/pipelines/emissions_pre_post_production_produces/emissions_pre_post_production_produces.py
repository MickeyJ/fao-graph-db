# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for emissions_pre_post_production PRODUCES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EmissionsPrePostProductionProducesMigrator(GraphMigrationBase):
    """Migrator for emissions_pre_post_production PRODUCES relationships"""
    
    def __init__(self):
        super().__init__("emissions_pre_post_production", "relationship")
        self.relationship_type = "PRODUCES"
        self.element_codes = ['717815', '7225', '7230', '723113', '723116', '723117', '723118', '723119', '723120', '7273']
        self.elements = ['Emissions (CO2eq) from F-gases (AR5)', 'Emissions (CH4)', 'Emissions (N2O)', 'Emissions (CO2eq) (AR5)', 'Energy Use (Natural Gas, including LNG)', 'Energy Use (Coal)', 'Energy Use (Electricity)', 'Energy Use (Heat)', 'Energy Use (Total)', 'Emissions (CO2)']
        self.relationship_properties = {"element": "Emissions (CO2)", "element_code": "7273", "measure": "other"}
    
    def get_migration_query(self) -> str:
        return load_sql("emissions_pre_post_production_produces.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("emissions_pre_post_production_produces_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("emissions_pre_post_production_produces_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for emissions_pre_post_production PRODUCES relationships"""
        logger.info(f"Starting emissions_pre_post_production PRODUCES relationship migration...")
        logger.info(f"  Elements: Emissions (CO2eq) from F-gases (AR5), Emissions (CH4), Emissions (N2O), Emissions (CO2eq) (AR5), Energy Use (Natural Gas, including LNG), Energy Use (Coal), Energy Use (Electricity), Energy Use (Heat), Energy Use (Total), Emissions (CO2)")
        logger.info(f"  Properties: {'measure': 'other', 'element_code': '7273', 'element': 'Emissions (CO2)'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} PRODUCES relationships from emissions_pre_post_production")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nemissions_pre_post_production relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate emissions_pre_post_production relationships: {e}")
            raise MigrationError(f"emissions_pre_post_production relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass