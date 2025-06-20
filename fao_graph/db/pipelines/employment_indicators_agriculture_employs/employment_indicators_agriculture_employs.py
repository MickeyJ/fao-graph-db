# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for employment_indicators_agriculture EMPLOYS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EmploymentIndicatorsAgricultureEmploysMigrator(GraphMigrationBase):
    """Migrator for employment_indicators_agriculture EMPLOYS relationships"""
    
    def __init__(self):
        super().__init__("employment_indicators_agriculture", "relationship")
        self.relationship_type = "EMPLOYS"
        
        self.indicator_codes = ['21110', '21066', '21086', '21088', '21089', '21090', '21091', '21093', '21097', '21100', '21107', '21111', '21144']
        
        self.relationship_properties = {"indicator": "Employment in agriculture by status of employment, workers not classified", "indicator_code": "21110", "indicator_codes": ["21110", "21066", "21086", "21088", "21089", "21090", "21091", "21093", "21097", "21100", "21107", "21111", "21144"]}
    
    def get_migration_query(self) -> str:
        return load_sql("employment_indicators_agriculture_employs.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("employment_indicators_agriculture_employs_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("employment_indicators_agriculture_employs_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for employment_indicators_agriculture EMPLOYS relationships"""
        logger.info(f"Starting employment_indicators_agriculture EMPLOYS relationship migration...")
        
        logger.info(f"  Filtering on indicator codes: 21110, 21066, 21086, 21088, 21089... (13 total)")
        
        logger.info(f"  Relationship type properties: {'indicator_codes': ['21110', '21066', '21086', '21088', '21089', '21090', '21091', '21093', '21097', '21100', '21107', '21111', '21144'], 'indicator': 'Employment in agriculture by status of employment, workers not classified', 'indicator_code': '21110'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMPLOYS relationships from employment_indicators_agriculture")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nemployment_indicators_agriculture relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate employment_indicators_agriculture relationships: {e}")
            raise MigrationError(f"employment_indicators_agriculture relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass