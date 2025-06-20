# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for production_crops_livestock PRODUCES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ProductionCropsLivestockProducesMigrator(GraphMigrationBase):
    """Migrator for production_crops_livestock PRODUCES relationships"""
    
    def __init__(self):
        super().__init__("production_crops_livestock", "relationship")
        self.relationship_type = "PRODUCES"
        self.element_codes = ['5510', '5419', '5312']
        self.elements = ['Production', 'Yield', 'Area harvested']
    
    def get_migration_query(self) -> str:
        return load_sql("production_crops_livestock_produces.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("production_crops_livestock_produces_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("production_crops_livestock_produces_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for production_crops_livestock PRODUCES relationships"""
        logger.info(f"Starting production_crops_livestock PRODUCES relationship migration...")
        logger.info(f"  Elements: Production, Yield, Area harvested")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                
                # Add source_table property for tracking
                query = query.replace(
                    "CREATE (source)-[r:PRODUCES {",
                    "CREATE (source)-[r:PRODUCES {source_dataset: 'production_crops_livestock', "
                )
                
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} PRODUCES relationships from production_crops_livestock")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nproduction_crops_livestock relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate production_crops_livestock relationships: {e}")
            raise MigrationError(f"production_crops_livestock relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass