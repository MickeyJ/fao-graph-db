# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for food_balance_sheets CONSUMES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class FoodBalanceSheetsConsumesMigrator(GraphMigrationBase):
    """Migrator for food_balance_sheets CONSUMES relationships"""
    
    def __init__(self):
        super().__init__("food_balance_sheets", "relationship")
        self.relationship_type = "CONSUMES"
        
        self.element_codes = ['5171', '5521', '645']
        
        self.relationship_properties = {"element": "Tourist consumption", "element_code": "5171", "element_codes": ["5171", "5521", "645"], "elements": true}
    
    def get_migration_query(self) -> str:
        return load_sql("food_balance_sheets_consumes.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("food_balance_sheets_consumes_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("food_balance_sheets_consumes_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for food_balance_sheets CONSUMES relationships"""
        logger.info(f"Starting food_balance_sheets CONSUMES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 5171, 5521, 645")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['5171', '5521', '645'], 'element': 'Tourist consumption', 'element_code': '5171', 'elements': True}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} CONSUMES relationships from food_balance_sheets")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nfood_balance_sheets relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate food_balance_sheets relationships: {e}")
            raise MigrationError(f"food_balance_sheets relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass