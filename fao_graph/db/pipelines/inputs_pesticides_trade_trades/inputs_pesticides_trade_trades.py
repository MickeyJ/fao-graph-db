# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for inputs_pesticides_trade TRADES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class InputsPesticidesTradeTradesMigrator(GraphMigrationBase):
    """Migrator for inputs_pesticides_trade TRADES relationships"""
    
    def __init__(self):
        super().__init__("inputs_pesticides_trade", "relationship")
        self.relationship_type = "TRADES"
        self.element_codes = ['5610', '5622', '5910', '5922']
        self.elements = ['Import quantity', 'Import value', 'Export quantity', 'Export value']
    
    def get_migration_query(self) -> str:
        return load_sql("inputs_pesticides_trade_trades.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("inputs_pesticides_trade_trades_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("inputs_pesticides_trade_trades_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for inputs_pesticides_trade TRADES relationships"""
        logger.info(f"Starting inputs_pesticides_trade TRADES relationship migration...")
        logger.info(f"  Elements: Import quantity, Import value, Export quantity, Export value")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                
                # Add source_table property for tracking
                query = query.replace(
                    "CREATE (source)-[r:TRADES {",
                    "CREATE (source)-[r:TRADES {source_dataset: 'inputs_pesticides_trade', "
                )
                
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} TRADES relationships from inputs_pesticides_trade")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ninputs_pesticides_trade relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate inputs_pesticides_trade relationships: {e}")
            raise MigrationError(f"inputs_pesticides_trade relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass