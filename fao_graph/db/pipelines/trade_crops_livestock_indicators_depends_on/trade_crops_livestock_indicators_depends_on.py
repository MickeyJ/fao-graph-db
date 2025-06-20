# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for trade_crops_livestock_indicators DEPENDS_ON relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class TradeCropsLivestockIndicatorsDepends_OnMigrator(GraphMigrationBase):
    """Migrator for trade_crops_livestock_indicators DEPENDS_ON relationships"""
    
    def __init__(self):
        super().__init__("trade_crops_livestock_indicators", "relationship")
        self.relationship_type = "DEPENDS_ON"
        self.relationship_properties = {"indicator": "Import dependency ratio", "indicator_code": "501", "measure": "import_dependency"}
    
    def get_migration_query(self) -> str:
        return load_sql("trade_crops_livestock_indicators_depends_on.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("trade_crops_livestock_indicators_depends_on_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("trade_crops_livestock_indicators_depends_on_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for trade_crops_livestock_indicators DEPENDS_ON relationships"""
        logger.info(f"Starting trade_crops_livestock_indicators DEPENDS_ON relationship migration...")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} DEPENDS_ON relationships from trade_crops_livestock_indicators")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ntrade_crops_livestock_indicators relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate trade_crops_livestock_indicators relationships: {e}")
            raise MigrationError(f"trade_crops_livestock_indicators relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass