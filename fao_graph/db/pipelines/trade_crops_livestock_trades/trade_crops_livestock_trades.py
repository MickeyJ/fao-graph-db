# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for trade_crops_livestock TRADES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class TradeCropsLivestockTradesMigrator(GraphMigrationBase):
    """Migrator for trade_crops_livestock TRADES relationships"""
    
    def __init__(self):
        super().__init__("trade_crops_livestock", "relationship")
        self.relationship_type = "TRADES"
        self.element_codes = ['50002', '50003', '50004', '50005', '50006', '50008', '50009', '50010', '50011', '50012', '50014', '50016', '50017', '50020', '50021', '50028', '5607', '5608', '5609', '5610', '5622', '5907', '5908', '5909', '5910', '5922', '66002', '66003', '66004', '66005', '66006', '66008', '66009', '66010', '66011', '66012', '66014', '66016', '66017', '66020', '66021', '66028']
        self.elements = ['Energy content of imports (kcal/capita/day)', 'Protein content of imports (g/capita/day)', 'Fat content of imports (g/capita/day)', 'Carbohydrate, available, content of imports (g/capita/day)', 'Dietary fibre content of imports (g/capita/day)', 'Calcium content of imports (mg/capita/day)', 'Iron content of imports (mg/capita/day)', 'Magnesium content of imports (mg/capita/day)', 'Phosphorus content of imports (mg/capita/day)', 'Potassium content of imports (mg/capita/day)', 'Zinc content of imports (mg/capita/day)', 'Vitamin A (RE) content of imports (mcg/capita/day)', 'Vitamin A (RAE) content of imports (mcg/capita/day)', 'Thiamin content of imports (mg/capita/day)', 'Riboflavin content of imports (mg/capita/day)', 'Vitamin C content of imports (mg/capita/day)', 'Import quantity', 'Import quantity', 'Import quantity', 'Import quantity', 'Import value', 'Export quantity', 'Export quantity', 'Export quantity', 'Export quantity', 'Export value', 'Energy content of exports (kcal/capita/day)', 'Protein content of exports (g/capita/day)', 'Fat content of exports (g/capita/day)', 'Carbohydrate, available, content of exports (g/capita/day)', 'Dietary fibre content of exports (g/capita/day)', 'Calcium content of exports (mg/capita/day)', 'Iron content of exports (mg/capita/day)', 'Magnesium content of exports (mg/capita/day)', 'Phosphorus content of exports (mg/capita/day)', 'Potassium content of exports (mg/capita/day)', 'Zinc content of exports (mg/capita/day)', 'Vitamin A (RE) content of exports (mcg/capita/day)', 'Vitamin A (RAE) content of exports (mcg/capita/day)', 'Thiamin content of exports (mg/capita/day)', 'Riboflavin content of exports (mg/capita/day)', 'Vitamin C content of exports (mg/capita/day)']
        self.relationship_properties = {"content_type": "nutrient", "element": "Vitamin C content of exports (mg/capita/day)", "element_code": "66028", "flow": "export", "measure": "content", "nutrient": "vitamin_c"}
    
    def get_migration_query(self) -> str:
        return load_sql("trade_crops_livestock_trades.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("trade_crops_livestock_trades_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("trade_crops_livestock_trades_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for trade_crops_livestock TRADES relationships"""
        logger.info(f"Starting trade_crops_livestock TRADES relationship migration...")
        logger.info(f"  Elements: Energy content of imports (kcal/capita/day), Protein content of imports (g/capita/day), Fat content of imports (g/capita/day), Carbohydrate, available, content of imports (g/capita/day), Dietary fibre content of imports (g/capita/day), Calcium content of imports (mg/capita/day), Iron content of imports (mg/capita/day), Magnesium content of imports (mg/capita/day), Phosphorus content of imports (mg/capita/day), Potassium content of imports (mg/capita/day), Zinc content of imports (mg/capita/day), Vitamin A (RE) content of imports (mcg/capita/day), Vitamin A (RAE) content of imports (mcg/capita/day), Thiamin content of imports (mg/capita/day), Riboflavin content of imports (mg/capita/day), Vitamin C content of imports (mg/capita/day), Import quantity, Import quantity, Import quantity, Import quantity, Import value, Export quantity, Export quantity, Export quantity, Export quantity, Export value, Energy content of exports (kcal/capita/day), Protein content of exports (g/capita/day), Fat content of exports (g/capita/day), Carbohydrate, available, content of exports (g/capita/day), Dietary fibre content of exports (g/capita/day), Calcium content of exports (mg/capita/day), Iron content of exports (mg/capita/day), Magnesium content of exports (mg/capita/day), Phosphorus content of exports (mg/capita/day), Potassium content of exports (mg/capita/day), Zinc content of exports (mg/capita/day), Vitamin A (RE) content of exports (mcg/capita/day), Vitamin A (RAE) content of exports (mcg/capita/day), Thiamin content of exports (mg/capita/day), Riboflavin content of exports (mg/capita/day), Vitamin C content of exports (mg/capita/day)")
        logger.info(f"  Properties: {'flow': 'export', 'content_type': 'nutrient', 'nutrient': 'vitamin_c', 'measure': 'content', 'element_code': '66028', 'element': 'Vitamin C content of exports (mg/capita/day)'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} TRADES relationships from trade_crops_livestock")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ntrade_crops_livestock relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate trade_crops_livestock relationships: {e}")
            raise MigrationError(f"trade_crops_livestock relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass