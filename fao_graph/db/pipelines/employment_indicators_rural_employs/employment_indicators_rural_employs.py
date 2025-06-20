# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for employment_indicators_rural EMPLOYS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EmploymentIndicatorsRuralEmploysMigrator(GraphMigrationBase):
    """Migrator for employment_indicators_rural EMPLOYS relationships"""
    
    def __init__(self):
        super().__init__("employment_indicators_rural", "relationship")
        self.relationship_type = "EMPLOYS"
        
        self.indicator_codes = ['21116', '21139', '21069', '21087', '21092', '21094', '21095', '21096', '21098', '21101', '21103', '21104', '21105', '21108', '21109', '21072', '21117', '21122', '21123', '21124']
        
        self.relationship_properties = {"indicator": "Employment by status of employment, workers not classified, rural areas", "indicator_code": "21116", "indicator_codes": ["21116", "21139", "21069", "21087", "21092", "21094", "21095", "21096", "21098", "21101", "21103", "21104", "21105", "21108", "21109", "21072", "21117", "21122", "21123", "21124"]}
    
    def get_migration_query(self) -> str:
        return load_sql("employment_indicators_rural_employs.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("employment_indicators_rural_employs_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("employment_indicators_rural_employs_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for employment_indicators_rural EMPLOYS relationships"""
        logger.info(f"Starting employment_indicators_rural EMPLOYS relationship migration...")
        
        logger.info(f"  Filtering on indicator codes: 21116, 21139, 21069, 21087, 21092... (20 total)")
        
        logger.info(f"  Relationship type properties: {'indicator_codes': ['21116', '21139', '21069', '21087', '21092', '21094', '21095', '21096', '21098', '21101', '21103', '21104', '21105', '21108', '21109', '21072', '21117', '21122', '21123', '21124'], 'indicator': 'Employment by status of employment, workers not classified, rural areas', 'indicator_code': '21116'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMPLOYS relationships from employment_indicators_rural")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nemployment_indicators_rural relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate employment_indicators_rural relationships: {e}")
            raise MigrationError(f"employment_indicators_rural relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass