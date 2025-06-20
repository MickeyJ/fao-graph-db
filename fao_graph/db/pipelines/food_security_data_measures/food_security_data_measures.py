# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for food_security_data MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class FoodSecurityDataMeasuresMigrator(GraphMigrationBase):
    """Migrator for food_security_data MEASURES relationships"""
    
    def __init__(self):
        super().__init__("food_security_data", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['6121', '61211', '61212', '6123', '6124', '6125', '6126', '6128', '6132', '61321', '61322', '6173']
        self.elements = ['Value', 'Confidence interval: Lower bound', 'Confidence interval: Upper bound', 'Value', 'Value', 'Value', 'Value', 'Value', 'Value', 'Confidence interval: Lower bound', 'Confidence interval: Upper bound', 'Value']
        self.relationship_properties = {"category": "general", "element": "Value", "element_code": "6173", "measure": "value"}
    
    def get_migration_query(self) -> str:
        return load_sql("food_security_data_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("food_security_data_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("food_security_data_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for food_security_data MEASURES relationships"""
        logger.info(f"Starting food_security_data MEASURES relationship migration...")
        logger.info(f"  Elements: Value, Confidence interval: Lower bound, Confidence interval: Upper bound, Value, Value, Value, Value, Value, Value, Confidence interval: Lower bound, Confidence interval: Upper bound, Value")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'value', 'element_code': '6173', 'element': 'Value'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from food_security_data")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nfood_security_data relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate food_security_data relationships: {e}")
            raise MigrationError(f"food_security_data relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass