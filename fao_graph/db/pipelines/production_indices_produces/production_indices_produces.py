# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for production_indices PRODUCES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ProductionIndicesProducesMigrator(GraphMigrationBase):
    """Migrator for production_indices PRODUCES relationships"""
    
    def __init__(self):
        super().__init__("production_indices", "relationship")
        self.relationship_type = "PRODUCES"
        self.element_codes = ['432', '434']
        self.elements = ['Gross Production Index Number (2014-2016 = 100)', 'Gross per capita Production Index Number (2014-2016 = 100)']
        self.relationship_properties = {"element": "Gross per capita Production Index Number (2014-2016 = 100)", "element_code": "434", "measure": "per_capita"}
    
    def get_migration_query(self) -> str:
        return load_sql("production_indices_produces.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("production_indices_produces_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("production_indices_produces_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for production_indices PRODUCES relationships"""
        logger.info(f"Starting production_indices PRODUCES relationship migration...")
        logger.info(f"  Elements: Gross Production Index Number (2014-2016 = 100), Gross per capita Production Index Number (2014-2016 = 100)")
        logger.info(f"  Properties: {'measure': 'per_capita', 'element_code': '434', 'element': 'Gross per capita Production Index Number (2014-2016 = 100)'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} PRODUCES relationships from production_indices")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nproduction_indices relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate production_indices relationships: {e}")
            raise MigrationError(f"production_indices relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass