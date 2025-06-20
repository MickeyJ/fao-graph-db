# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for minimum_dietary_diversity_for_women_mdd_w_food_and_diet MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class MinimumDietaryDiversityForWomenMddWFoodAndDietMeasuresMigrator(GraphMigrationBase):
    """Migrator for minimum_dietary_diversity_for_women_mdd_w_food_and_diet MEASURES relationships"""
    
    def __init__(self):
        super().__init__("minimum_dietary_diversity_for_women_mdd_w_food_and_diet", "relationship")
        self.relationship_type = "MEASURES"
    
    def get_migration_query(self) -> str:
        return load_sql("minimum_dietary_diversity_for_women_mdd_w_food_and_diet_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("minimum_dietary_diversity_for_women_mdd_w_food_and_diet_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("minimum_dietary_diversity_for_women_mdd_w_food_and_diet_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for minimum_dietary_diversity_for_women_mdd_w_food_and_diet MEASURES relationships"""
        logger.info(f"Starting minimum_dietary_diversity_for_women_mdd_w_food_and_diet MEASURES relationship migration...")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from minimum_dietary_diversity_for_women_mdd_w_food_and_diet")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nminimum_dietary_diversity_for_women_mdd_w_food_and_diet relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate minimum_dietary_diversity_for_women_mdd_w_food_and_diet relationships: {e}")
            raise MigrationError(f"minimum_dietary_diversity_for_women_mdd_w_food_and_diet relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass