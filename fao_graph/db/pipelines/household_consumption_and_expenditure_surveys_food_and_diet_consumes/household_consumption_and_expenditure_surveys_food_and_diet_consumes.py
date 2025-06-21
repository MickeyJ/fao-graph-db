# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for household_consumption_and_expenditure_surveys_food_and_diet CONSUMES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class HouseholdConsumptionAndExpenditureSurveysFoodAndDietConsumesMigrator(GraphMigrationBase):
    """Migrator for household_consumption_and_expenditure_surveys_food_and_diet CONSUMES relationships"""
    
    def __init__(self):
        super().__init__("household_consumption_and_expenditure_surveys_food_and_diet", "relationship")
        self.relationship_type = "CONSUMES"
        
        self.indicator_codes = ['3302', '3303', '3304', '3305', '3306', '3307', '3308', '3309', '3310', '3311', '3312', '3313', '3314', '3315', '3316', '3317', '3318', '3319', '3300']
        
        self.relationship_properties = {"indicator": "Energy apparent intake", "indicator_code": "3302", "indicator_codes": ["3302", "3303", "3304", "3305", "3306", "3307", "3308", "3309", "3310", "3311", "3312", "3313", "3314", "3315", "3316", "3317", "3318", "3319", "3300"], "indicators": true}
    
    def get_migration_query(self) -> str:
        return load_sql("household_consumption_and_expenditure_surveys_food_and_diet_consumes.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("household_consumption_and_expenditure_surveys_food_and_diet_consumes_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("household_consumption_and_expenditure_surveys_food_and_diet_consumes_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for household_consumption_and_expenditure_surveys_food_and_diet CONSUMES relationships"""
        logger.info(f"Starting household_consumption_and_expenditure_surveys_food_and_diet CONSUMES relationship migration...")
        
        logger.info(f"  Filtering on indicator codes: 3302, 3303, 3304, 3305, 3306... (19 total)")
        
        logger.info(f"  Relationship type properties: {'indicator_codes': ['3302', '3303', '3304', '3305', '3306', '3307', '3308', '3309', '3310', '3311', '3312', '3313', '3314', '3315', '3316', '3317', '3318', '3319', '3300'], 'indicator': 'Energy apparent intake', 'indicator_code': '3302', 'indicators': True}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} CONSUMES relationships from household_consumption_and_expenditure_surveys_food_and_diet")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nhousehold_consumption_and_expenditure_surveys_food_and_diet relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate household_consumption_and_expenditure_surveys_food_and_diet relationships: {e}")
            raise MigrationError(f"household_consumption_and_expenditure_surveys_food_and_diet relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass