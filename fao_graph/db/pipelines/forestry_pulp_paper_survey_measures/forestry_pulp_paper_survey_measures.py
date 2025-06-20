# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for forestry_pulp_paper_survey MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ForestryPulpPaperSurveyMeasuresMigrator(GraphMigrationBase):
    """Migrator for forestry_pulp_paper_survey MEASURES relationships"""
    
    def __init__(self):
        super().__init__("forestry_pulp_paper_survey", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5034', '5326', '5510', '5800', '5801']
        self.elements = ['Consumption', 'Capacity', 'Production', 'Market pulp Capacity', 'Market pulp Production']
        self.relationship_properties = {"category": "general", "element": "Market pulp Production", "element_code": "5801", "measure": "other"}
    
    def get_migration_query(self) -> str:
        return load_sql("forestry_pulp_paper_survey_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("forestry_pulp_paper_survey_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("forestry_pulp_paper_survey_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for forestry_pulp_paper_survey MEASURES relationships"""
        logger.info(f"Starting forestry_pulp_paper_survey MEASURES relationship migration...")
        logger.info(f"  Elements: Consumption, Capacity, Production, Market pulp Capacity, Market pulp Production")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'other', 'element_code': '5801', 'element': 'Market pulp Production'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from forestry_pulp_paper_survey")
            
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