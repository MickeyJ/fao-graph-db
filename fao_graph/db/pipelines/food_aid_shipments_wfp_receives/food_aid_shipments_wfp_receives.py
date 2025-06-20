# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for food_aid_shipments_wfp RECEIVES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class FoodAidShipmentsWfpReceivesMigrator(GraphMigrationBase):
    """Migrator for food_aid_shipments_wfp RECEIVES relationships"""
    
    def __init__(self):
        super().__init__("food_aid_shipments_wfp", "relationship")
        self.relationship_type = "RECEIVES"
    
    def get_migration_query(self) -> str:
        return load_sql("food_aid_shipments_wfp_receives.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("food_aid_shipments_wfp_receives_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("food_aid_shipments_wfp_receives_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for food_aid_shipments_wfp RECEIVES relationships"""
        logger.info(f"Starting food_aid_shipments_wfp RECEIVES relationship migration...")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} RECEIVES relationships from food_aid_shipments_wfp")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nfood_aid_shipments_wfp relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate food_aid_shipments_wfp relationships: {e}")
            raise MigrationError(f"food_aid_shipments_wfp relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass