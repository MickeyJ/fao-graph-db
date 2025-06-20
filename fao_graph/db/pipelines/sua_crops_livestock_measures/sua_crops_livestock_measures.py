# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for sua_crops_livestock MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class SuaCropsLivestockMeasuresMigrator(GraphMigrationBase):
    """Migrator for sua_crops_livestock MEASURES relationships"""
    
    def __init__(self):
        super().__init__("sua_crops_livestock", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['261', '271', '281', '5016', '5023', '5071', '511', '5113', '5164', '5166', '5525']
        self.elements = ['Calories/Year', 'Proteins/Year', 'Fats/Year', 'Loss', 'Processed', 'Stock Variation', 'Total Population - Both sexes', 'Opening stocks', 'Tourist consumption', 'Residuals', 'Seed']
        self.relationship_properties = {"category": "food_balance", "element": "Seed", "element_code": "5525", "measure": "other"}
    
    def get_migration_query(self) -> str:
        return load_sql("sua_crops_livestock_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("sua_crops_livestock_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("sua_crops_livestock_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for sua_crops_livestock MEASURES relationships"""
        logger.info(f"Starting sua_crops_livestock MEASURES relationship migration...")
        logger.info(f"  Elements: Calories/Year, Proteins/Year, Fats/Year, Loss, Processed, Stock Variation, Total Population - Both sexes, Opening stocks, Tourist consumption, Residuals, Seed")
        logger.info(f"  Properties: {'category': 'food_balance', 'measure': 'other', 'element_code': '5525', 'element': 'Seed'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from sua_crops_livestock")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nsua_crops_livestock relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate sua_crops_livestock relationships: {e}")
            raise MigrationError(f"sua_crops_livestock relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass