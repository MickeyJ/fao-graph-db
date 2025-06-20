# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for prices_archive MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class PricesArchiveMeasuresMigrator(GraphMigrationBase):
    """Migrator for prices_archive MEASURES relationships"""
    
    def __init__(self):
        super().__init__("prices_archive", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5530']
        self.elements = ['Producer Price (LCU/tonne)']
        self.relationship_properties = {"category": "price", "currency": "local", "element": "Producer Price (LCU/tonne)", "element_code": "5530", "price_type": "producer"}
    
    def get_migration_query(self) -> str:
        return load_sql("prices_archive_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("prices_archive_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("prices_archive_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for prices_archive MEASURES relationships"""
        logger.info(f"Starting prices_archive MEASURES relationship migration...")
        logger.info(f"  Elements: Producer Price (LCU/tonne)")
        logger.info(f"  Properties: {'category': 'price', 'price_type': 'producer', 'currency': 'local', 'element_code': '5530', 'element': 'Producer Price (LCU/tonne)'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from prices_archive")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nprices_archive relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate prices_archive relationships: {e}")
            raise MigrationError(f"prices_archive relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass