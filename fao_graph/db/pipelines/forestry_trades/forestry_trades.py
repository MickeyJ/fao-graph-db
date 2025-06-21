# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for forestry TRADES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ForestryTradesMigrator(GraphMigrationBase):
    """Migrator for forestry TRADES relationships"""
    
    def __init__(self):
        super().__init__("forestry", "relationship")
        self.relationship_type = "TRADES"
        
        self.element_codes = ['5610', '5616', '5622', '5910', '5916', '5922']
        
        self.relationship_properties = {"element": "Import quantity", "element_code": "5610", "element_codes": ["5610", "5616", "5622", "5910", "5916", "5922"], "elements": true, "flow_direction": "bidirectional"}
    
    def get_migration_query(self) -> str:
        return load_sql("forestry_trades.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("forestry_trades_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("forestry_trades_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for forestry TRADES relationships"""
        logger.info(f"Starting forestry TRADES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 5610, 5616, 5622, 5910, 5916... (6 total)")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['5610', '5616', '5622', '5910', '5916', '5922'], 'element': 'Import quantity', 'element_code': '5610', 'elements': True, 'flow_direction': 'bidirectional'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} TRADES relationships from forestry")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nforestry relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate forestry relationships: {e}")
            raise MigrationError(f"forestry relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass