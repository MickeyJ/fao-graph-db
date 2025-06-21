# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for asti_expenditures MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class AstiExpendituresMeasuresMigrator(GraphMigrationBase):
    """Migrator for asti_expenditures MEASURES relationships"""
    
    def __init__(self):
        super().__init__("asti_expenditures", "relationship")
        self.relationship_type = "MEASURES"
        
        self.element_codes = ['6083']
        
        self.relationship_properties = {"element": "Share of Value Added (Agriculture, Forestry and Fishing)", "element_code": "6083", "element_codes": ["6083"], "elements": true}
    
    def get_migration_query(self) -> str:
        return load_sql("asti_expenditures_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("asti_expenditures_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("asti_expenditures_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for asti_expenditures MEASURES relationships"""
        logger.info(f"Starting asti_expenditures MEASURES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 6083")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['6083'], 'element': 'Share of Value Added (Agriculture, Forestry and Fishing)', 'element_code': '6083', 'elements': True}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from asti_expenditures")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nasti_expenditures relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate asti_expenditures relationships: {e}")
            raise MigrationError(f"asti_expenditures relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass