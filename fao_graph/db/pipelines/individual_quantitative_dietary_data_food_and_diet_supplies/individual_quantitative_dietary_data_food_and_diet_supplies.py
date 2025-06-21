# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for individual_quantitative_dietary_data_food_and_diet SUPPLIES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class IndividualQuantitativeDietaryDataFoodAndDietSuppliesMigrator(GraphMigrationBase):
    """Migrator for individual_quantitative_dietary_data_food_and_diet SUPPLIES relationships"""
    
    def __init__(self):
        super().__init__("individual_quantitative_dietary_data_food_and_diet", "relationship")
        self.relationship_type = "SUPPLIES"
        
        self.element_codes = ['6120', '6121', '6123', '6128', '6206', '6209']
        
        self.relationship_properties = {"element": "Value", "element_code": "6120", "element_codes": ["6120", "6121", "6123", "6128", "6206", "6209"], "elements": true}
    
    def get_migration_query(self) -> str:
        return load_sql("individual_quantitative_dietary_data_food_and_diet_supplies.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("individual_quantitative_dietary_data_food_and_diet_supplies_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("individual_quantitative_dietary_data_food_and_diet_supplies_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for individual_quantitative_dietary_data_food_and_diet SUPPLIES relationships"""
        logger.info(f"Starting individual_quantitative_dietary_data_food_and_diet SUPPLIES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 6120, 6121, 6123, 6128, 6206... (6 total)")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['6120', '6121', '6123', '6128', '6206', '6209'], 'element': 'Value', 'element_code': '6120', 'elements': True}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} SUPPLIES relationships from individual_quantitative_dietary_data_food_and_diet")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nindividual_quantitative_dietary_data_food_and_diet relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate individual_quantitative_dietary_data_food_and_diet relationships: {e}")
            raise MigrationError(f"individual_quantitative_dietary_data_food_and_diet relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass