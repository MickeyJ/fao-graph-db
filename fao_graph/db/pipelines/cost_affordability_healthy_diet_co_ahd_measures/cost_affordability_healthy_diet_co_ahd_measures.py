# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for cost_affordability_healthy_diet_co_ahd MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class CostAffordabilityHealthyDietCoAhdMeasuresMigrator(GraphMigrationBase):
    """Migrator for cost_affordability_healthy_diet_co_ahd MEASURES relationships"""
    
    def __init__(self):
        super().__init__("cost_affordability_healthy_diet_co_ahd", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['6121', '6132', '6226']
        self.elements = ['Value', 'Value', 'Value']
        self.relationship_properties = {"category": "general", "element": "Value", "element_code": "6226", "measure": "value"}
    
    def get_migration_query(self) -> str:
        return load_sql("cost_affordability_healthy_diet_co_ahd_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("cost_affordability_healthy_diet_co_ahd_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("cost_affordability_healthy_diet_co_ahd_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for cost_affordability_healthy_diet_co_ahd MEASURES relationships"""
        logger.info(f"Starting cost_affordability_healthy_diet_co_ahd MEASURES relationship migration...")
        logger.info(f"  Elements: Value, Value, Value")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'value', 'element_code': '6226', 'element': 'Value'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from cost_affordability_healthy_diet_co_ahd")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ncost_affordability_healthy_diet_co_ahd relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate cost_affordability_healthy_diet_co_ahd relationships: {e}")
            raise MigrationError(f"cost_affordability_healthy_diet_co_ahd relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass