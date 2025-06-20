# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for food_balance_sheets_historic USES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class FoodBalanceSheetsHistoricUsesMigrator(GraphMigrationBase):
    """Migrator for food_balance_sheets_historic USES relationships"""
    
    def __init__(self):
        super().__init__("food_balance_sheets_historic", "relationship")
        self.relationship_type = "USES"
        self.element_codes = ['5142', '5521']
        self.elements = ['Food', 'Feed']
    
    def get_migration_query(self) -> str:
        return load_sql("food_balance_sheets_historic_uses.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("food_balance_sheets_historic_uses_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("food_balance_sheets_historic_uses_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for food_balance_sheets_historic USES relationships"""
        logger.info(f"Starting food_balance_sheets_historic USES relationship migration...")
        logger.info(f"  Elements: Food, Feed")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                
                # Add source_table property for tracking
                query = query.replace(
                    "CREATE (source)-[r:USES {",
                    "CREATE (source)-[r:USES {source_dataset: 'food_balance_sheets_historic', "
                )
                
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} USES relationships from food_balance_sheets_historic")
            
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