# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for food_balance_sheets_historic IMPACTS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class FoodBalanceSheetsHistoricImpactsMigrator(GraphMigrationBase):
    """Migrator for food_balance_sheets_historic IMPACTS relationships"""
    
    def __init__(self):
        super().__init__("food_balance_sheets_historic", "relationship")
        self.relationship_type = "IMPACTS"
        
        self.element_codes = ['5123']
        
        self.relationship_properties = {"element": "Losses", "element_code": "5123", "element_codes": ["5123"], "elements": true}
    
    def get_migration_query(self) -> str:
        return load_sql("food_balance_sheets_historic_impacts.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("food_balance_sheets_historic_impacts_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("food_balance_sheets_historic_impacts_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for food_balance_sheets_historic IMPACTS relationships"""
        logger.info(f"Starting food_balance_sheets_historic IMPACTS relationship migration...")
        
        logger.info(f"  Filtering on element codes: 5123")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['5123'], 'element': 'Losses', 'element_code': '5123', 'elements': True}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} IMPACTS relationships from food_balance_sheets_historic")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nfood_balance_sheets_historic relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate food_balance_sheets_historic relationships: {e}")
            raise MigrationError(f"food_balance_sheets_historic relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass