# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for prices MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class PricesMeasuresMigrator(GraphMigrationBase):
    """Migrator for prices MEASURES relationships"""
    
    def __init__(self):
        super().__init__("prices", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5530', '5532']
        self.elements = ['Producer Price (LCU/tonne)', 'Producer Price (USD/tonne)']
    
    def get_migration_query(self) -> str:
        return load_sql("prices_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("prices_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("prices_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for prices MEASURES relationships"""
        logger.info(f"Starting prices MEASURES relationship migration...")
        logger.info(f"  Elements: Producer Price (LCU/tonne), Producer Price (USD/tonne)")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                
                # Add source_table property for tracking
                query = query.replace(
                    "CREATE (source)-[r:MEASURES {",
                    "CREATE (source)-[r:MEASURES {source_dataset: 'prices', "
                )
                
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from prices")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nprices relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate prices relationships: {e}")
            raise MigrationError(f"prices relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass