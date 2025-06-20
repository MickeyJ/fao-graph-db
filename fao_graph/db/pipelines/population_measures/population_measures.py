# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for population MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class PopulationMeasuresMigrator(GraphMigrationBase):
    """Migrator for population MEASURES relationships"""
    
    def __init__(self):
        super().__init__("population", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['511', '512', '513', '551', '561']
        self.elements = ['Total Population - Both sexes', 'Total Population - Male', 'Total Population - Female', 'Rural population', 'Urban population']
        self.relationship_properties = {"category": "general", "element": "Urban population", "element_code": "561", "measure": "other"}
    
    def get_migration_query(self) -> str:
        return load_sql("population_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("population_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("population_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for population MEASURES relationships"""
        logger.info(f"Starting population MEASURES relationship migration...")
        logger.info(f"  Elements: Total Population - Both sexes, Total Population - Male, Total Population - Female, Rural population, Urban population")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'other', 'element_code': '561', 'element': 'Urban population'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from population")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\npopulation relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate population relationships: {e}")
            raise MigrationError(f"population relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass