# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for consumer_price_indices MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ConsumerPriceIndicesMeasuresMigrator(GraphMigrationBase):
    """Migrator for consumer_price_indices MEASURES relationships"""
    
    def __init__(self):
        super().__init__("consumer_price_indices", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5110']
        self.elements = ['Value']
    
    def get_migration_query(self) -> str:
        return load_sql("consumer_price_indices_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("consumer_price_indices_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("consumer_price_indices_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for consumer_price_indices MEASURES relationships"""
        logger.info(f"Starting consumer_price_indices MEASURES relationship migration...")
        logger.info(f"  Elements: Value")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                
                # Add source_table property for tracking
                query = query.replace(
                    "CREATE (source)-[r:MEASURES {",
                    "CREATE (source)-[r:MEASURES {source_dataset: 'consumer_price_indices', "
                )
                
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from consumer_price_indices")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nconsumer_price_indices relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate consumer_price_indices relationships: {e}")
            raise MigrationError(f"consumer_price_indices relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass