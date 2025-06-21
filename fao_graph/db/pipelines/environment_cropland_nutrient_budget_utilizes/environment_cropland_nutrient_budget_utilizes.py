# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for environment_cropland_nutrient_budget UTILIZES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EnvironmentCroplandNutrientBudgetUtilizesMigrator(GraphMigrationBase):
    """Migrator for environment_cropland_nutrient_budget UTILIZES relationships"""
    
    def __init__(self):
        super().__init__("environment_cropland_nutrient_budget", "relationship")
        self.relationship_type = "UTILIZES"
        
        self.element_codes = ['7290', '7291', '7292']
        
        self.relationship_properties = {"element": "Cropland nitrogen use efficiency", "element_code": "7290", "element_codes": ["7290", "7291", "7292"], "elements": true}
    
    def get_migration_query(self) -> str:
        return load_sql("environment_cropland_nutrient_budget_utilizes.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("environment_cropland_nutrient_budget_utilizes_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("environment_cropland_nutrient_budget_utilizes_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for environment_cropland_nutrient_budget UTILIZES relationships"""
        logger.info(f"Starting environment_cropland_nutrient_budget UTILIZES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 7290, 7291, 7292")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['7290', '7291', '7292'], 'element': 'Cropland nitrogen use efficiency', 'element_code': '7290', 'elements': True}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} UTILIZES relationships from environment_cropland_nutrient_budget")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nenvironment_cropland_nutrient_budget relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate environment_cropland_nutrient_budget relationships: {e}")
            raise MigrationError(f"environment_cropland_nutrient_budget relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass