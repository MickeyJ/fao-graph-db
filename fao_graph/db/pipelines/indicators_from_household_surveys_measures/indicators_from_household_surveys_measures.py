# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for indicators_from_household_surveys MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class IndicatorsFromHouseholdSurveysMeasuresMigrator(GraphMigrationBase):
    """Migrator for indicators_from_household_surveys MEASURES relationships"""
    
    def __init__(self):
        super().__init__("indicators_from_household_surveys", "relationship")
        self.relationship_type = "MEASURES"
    
    def get_migration_query(self) -> str:
        return load_sql("indicators_from_household_surveys_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("indicators_from_household_surveys_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("indicators_from_household_surveys_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for indicators_from_household_surveys MEASURES relationships"""
        logger.info(f"Starting indicators_from_household_surveys MEASURES relationship migration...")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from indicators_from_household_surveys")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nindicators_from_household_surveys relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate indicators_from_household_surveys relationships: {e}")
            raise MigrationError(f"indicators_from_household_surveys relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass