# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for food_balance_sheets MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class FoodBalanceSheetsMeasuresMigrator(GraphMigrationBase):
    """Migrator for food_balance_sheets MEASURES relationships"""
    
    def __init__(self):
        super().__init__("food_balance_sheets", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5072', '511', '5123', '5131', '5170', '5171', '5301', '5527']
        self.elements = ['Stock Variation', 'Total Population - Both sexes', 'Losses', 'Processing', 'Residuals', 'Tourist consumption', 'Domestic supply quantity', 'Seed']
        self.relationship_properties = {"category": "food_balance", "element": "Seed", "element_code": "5527", "measure": "other"}
    
    def get_migration_query(self) -> str:
        return load_sql("food_balance_sheets_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("food_balance_sheets_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("food_balance_sheets_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for food_balance_sheets MEASURES relationships"""
        logger.info(f"Starting food_balance_sheets MEASURES relationship migration...")
        logger.info(f"  Elements: Stock Variation, Total Population - Both sexes, Losses, Processing, Residuals, Tourist consumption, Domestic supply quantity, Seed")
        logger.info(f"  Properties: {'category': 'food_balance', 'measure': 'other', 'element_code': '5527', 'element': 'Seed'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from food_balance_sheets")
            
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