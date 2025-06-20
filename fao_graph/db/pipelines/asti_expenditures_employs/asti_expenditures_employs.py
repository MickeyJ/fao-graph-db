# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for asti_expenditures EMPLOYS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class AstiExpendituresEmploysMigrator(GraphMigrationBase):
    """Migrator for asti_expenditures EMPLOYS relationships"""
    
    def __init__(self):
        super().__init__("asti_expenditures", "relationship")
        self.relationship_type = "EMPLOYS"
        self.element_codes = ['6083', '6084']
        self.elements = ['Share of Value Added (Agriculture, Forestry and Fishing)', 'Spending, total (constant 2011 prices)']
        self.relationship_properties = {"element": "Spending, total (constant 2011 prices)", "element_code": "6084", "measure": "other", "role": "worker"}
    
    def get_migration_query(self) -> str:
        return load_sql("asti_expenditures_employs.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("asti_expenditures_employs_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("asti_expenditures_employs_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for asti_expenditures EMPLOYS relationships"""
        logger.info(f"Starting asti_expenditures EMPLOYS relationship migration...")
        logger.info(f"  Elements: Share of Value Added (Agriculture, Forestry and Fishing), Spending, total (constant 2011 prices)")
        logger.info(f"  Properties: {'role': 'worker', 'measure': 'other', 'element_code': '6084', 'element': 'Spending, total (constant 2011 prices)'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMPLOYS relationships from asti_expenditures")
            
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