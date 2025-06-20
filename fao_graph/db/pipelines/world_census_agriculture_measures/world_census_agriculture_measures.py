# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for world_census_agriculture MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class WorldCensusAgricultureMeasuresMigrator(GraphMigrationBase):
    """Migrator for world_census_agriculture MEASURES relationships"""
    
    def __init__(self):
        super().__init__("world_census_agriculture", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5017', '5018', '50190', '50191', '50260', '60850', '6200', '6201', '62020', '62021']
        self.elements = ['Average area', 'Average number of parcels per holding', 'Average persons per holding (household members)', 'Average persons per holding (hired permanent workers)', 'Area', 'Number', 'Percentage of total area', 'Percent of total number', 'Percent of total persons (holders)', 'Percent of total persons (household members)']
        self.relationship_properties = {"category": "general", "element": "Percent of total persons (household members)", "element_code": "62021", "measure": "other"}
    
    def get_migration_query(self) -> str:
        return load_sql("world_census_agriculture_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("world_census_agriculture_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("world_census_agriculture_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for world_census_agriculture MEASURES relationships"""
        logger.info(f"Starting world_census_agriculture MEASURES relationship migration...")
        logger.info(f"  Elements: Average area, Average number of parcels per holding, Average persons per holding (household members), Average persons per holding (hired permanent workers), Area, Number, Percentage of total area, Percent of total number, Percent of total persons (holders), Percent of total persons (household members)")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'other', 'element_code': '62021', 'element': 'Percent of total persons (household members)'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from world_census_agriculture")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nworld_census_agriculture relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate world_census_agriculture relationships: {e}")
            raise MigrationError(f"world_census_agriculture relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass