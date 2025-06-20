# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for asti_researchers EMPLOYS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class AstiResearchersEmploysMigrator(GraphMigrationBase):
    """Migrator for asti_researchers EMPLOYS relationships"""
    
    def __init__(self):
        super().__init__("asti_researchers", "relationship")
        self.relationship_type = "EMPLOYS"
        self.element_codes = ['6082', '6086']
        self.elements = ['Researchers, total', 'Per 100,000 farmers']
        self.relationship_properties = {"element": "Per 100,000 farmers", "element_code": "6086", "measure": "other", "role": "worker"}
    
    def get_migration_query(self) -> str:
        return load_sql("asti_researchers_employs.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("asti_researchers_employs_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("asti_researchers_employs_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for asti_researchers EMPLOYS relationships"""
        logger.info(f"Starting asti_researchers EMPLOYS relationship migration...")
        logger.info(f"  Elements: Researchers, total, Per 100,000 farmers")
        logger.info(f"  Properties: {'role': 'worker', 'measure': 'other', 'element_code': '6086', 'element': 'Per 100,000 farmers'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMPLOYS relationships from asti_researchers")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nasti_researchers relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate asti_researchers relationships: {e}")
            raise MigrationError(f"asti_researchers relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass