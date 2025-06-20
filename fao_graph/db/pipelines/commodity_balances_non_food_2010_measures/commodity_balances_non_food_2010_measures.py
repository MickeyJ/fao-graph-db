# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for commodity_balances_non_food_2010 MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class CommodityBalancesNonFood2010MeasuresMigrator(GraphMigrationBase):
    """Migrator for commodity_balances_non_food_2010 MEASURES relationships"""
    
    def __init__(self):
        super().__init__("commodity_balances_non_food_2010", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5023', '5071', '5165', '5166', '5510', '5610', '5910']
        self.elements = ['Processed', 'Stock Variation', 'Other uses (non-food)', 'Residuals', 'Production', 'Import quantity', 'Export quantity']
        self.relationship_properties = {"category": "general", "element": "Export quantity", "element_code": "5910", "measure": "quantity"}
    
    def get_migration_query(self) -> str:
        return load_sql("commodity_balances_non_food_2010_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("commodity_balances_non_food_2010_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("commodity_balances_non_food_2010_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for commodity_balances_non_food_2010 MEASURES relationships"""
        logger.info(f"Starting commodity_balances_non_food_2010 MEASURES relationship migration...")
        logger.info(f"  Elements: Processed, Stock Variation, Other uses (non-food), Residuals, Production, Import quantity, Export quantity")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'quantity', 'element_code': '5910', 'element': 'Export quantity'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from commodity_balances_non_food_2010")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ncommodity_balances_non_food_2010 relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate commodity_balances_non_food_2010 relationships: {e}")
            raise MigrationError(f"commodity_balances_non_food_2010 relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass