# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for food_balance_sheets_historic SUPPLIES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class FoodBalanceSheetsHistoricSuppliesMigrator(GraphMigrationBase):
    """Migrator for food_balance_sheets_historic SUPPLIES relationships"""
    
    def __init__(self):
        super().__init__("food_balance_sheets_historic", "relationship")
        self.relationship_type = "SUPPLIES"
        
        self.element_codes = ['674', '684', '664', '5074', '5131', '5142', '5301', '5527']
        
        self.relationship_properties = {"element": "Protein supply quantity (g/capita/day)", "element_code": "674", "element_codes": ["674", "684", "664", "5074", "5131", "5142", "5301", "5527"], "elements": true, "nutrient_type": "protein"}
    
    def get_migration_query(self) -> str:
        return load_sql("food_balance_sheets_historic_supplies.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("food_balance_sheets_historic_supplies_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("food_balance_sheets_historic_supplies_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for food_balance_sheets_historic SUPPLIES relationships"""
        logger.info(f"Starting food_balance_sheets_historic SUPPLIES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 674, 684, 664, 5074, 5131... (8 total)")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['674', '684', '664', '5074', '5131', '5142', '5301', '5527'], 'element': 'Protein supply quantity (g/capita/day)', 'element_code': '674', 'elements': True, 'nutrient_type': 'protein'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} SUPPLIES relationships from food_balance_sheets_historic")
            
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