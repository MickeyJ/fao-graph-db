# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for inputs_fertilizers_nutrient TRADES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class InputsFertilizersNutrientTradesMigrator(GraphMigrationBase):
    """Migrator for inputs_fertilizers_nutrient TRADES relationships"""
    
    def __init__(self):
        super().__init__("inputs_fertilizers_nutrient", "relationship")
        self.relationship_type = "TRADES"
        self.element_codes = ['5610', '5910']
        self.elements = ['Import quantity', 'Export quantity']
        self.relationship_properties = {"commodity_type": "agricultural_inputs", "element": "Export quantity", "element_code": "5910", "flow": "export"}
    
    def get_migration_query(self) -> str:
        return load_sql("inputs_fertilizers_nutrient_trades.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("inputs_fertilizers_nutrient_trades_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("inputs_fertilizers_nutrient_trades_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for inputs_fertilizers_nutrient TRADES relationships"""
        logger.info(f"Starting inputs_fertilizers_nutrient TRADES relationship migration...")
        logger.info(f"  Elements: Import quantity, Export quantity")
        logger.info(f"  Properties: {'flow': 'export', 'commodity_type': 'agricultural_inputs', 'element_code': '5910', 'element': 'Export quantity'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} TRADES relationships from inputs_fertilizers_nutrient")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ninputs_fertilizers_nutrient relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate inputs_fertilizers_nutrient relationships: {e}")
            raise MigrationError(f"inputs_fertilizers_nutrient relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass