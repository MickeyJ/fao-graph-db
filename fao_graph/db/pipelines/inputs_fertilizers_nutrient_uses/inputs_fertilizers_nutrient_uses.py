# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for inputs_fertilizers_nutrient USES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class InputsFertilizersNutrientUsesMigrator(GraphMigrationBase):
    """Migrator for inputs_fertilizers_nutrient USES relationships"""
    
    def __init__(self):
        super().__init__("inputs_fertilizers_nutrient", "relationship")
        self.relationship_type = "USES"
        self.element_codes = ['5157', '5159']
        self.elements = ['Agricultural Use', 'Use per area of cropland']
    
    def get_migration_query(self) -> str:
        return load_sql("inputs_fertilizers_nutrient_uses.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("inputs_fertilizers_nutrient_uses_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("inputs_fertilizers_nutrient_uses_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for inputs_fertilizers_nutrient USES relationships"""
        logger.info(f"Starting inputs_fertilizers_nutrient USES relationship migration...")
        logger.info(f"  Elements: Agricultural Use, Use per area of cropland")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                
                # Add source_table property for tracking
                query = query.replace(
                    "CREATE (source)-[r:USES {",
                    "CREATE (source)-[r:USES {source_dataset: 'inputs_fertilizers_nutrient', "
                )
                
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} USES relationships from inputs_fertilizers_nutrient")
            
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