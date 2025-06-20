# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for forestry_pulp_paper_survey CONSUMES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ForestryPulpPaperSurveyConsumesMigrator(GraphMigrationBase):
    """Migrator for forestry_pulp_paper_survey CONSUMES relationships"""
    
    def __init__(self):
        super().__init__("forestry_pulp_paper_survey", "relationship")
        self.relationship_type = "CONSUMES"
        
        self.element_codes = ['5034']
        
        self.relationship_properties = {"element": "Consumption", "element_code": "5034", "element_codes": ["5034"]}
    
    def get_migration_query(self) -> str:
        return load_sql("forestry_pulp_paper_survey_consumes.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("forestry_pulp_paper_survey_consumes_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("forestry_pulp_paper_survey_consumes_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for forestry_pulp_paper_survey CONSUMES relationships"""
        logger.info(f"Starting forestry_pulp_paper_survey CONSUMES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 5034")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['5034'], 'element': 'Consumption', 'element_code': '5034'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} CONSUMES relationships from forestry_pulp_paper_survey")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nforestry_pulp_paper_survey relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate forestry_pulp_paper_survey relationships: {e}")
            raise MigrationError(f"forestry_pulp_paper_survey relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass