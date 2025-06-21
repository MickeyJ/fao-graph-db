# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for trade_crops_livestock TRADES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class TradeCropsLivestockTradesMigrator(GraphMigrationBase):
    """Migrator for trade_crops_livestock TRADES relationships"""
    
    def __init__(self):
        super().__init__("trade_crops_livestock", "relationship")
        self.relationship_type = "TRADES"
        
        self.element_codes = ['5607', '5608', '5609', '5610', '5622', '5907', '5908', '5909', '5910', '5922', '50002', '50003', '50004', '50005', '50006', '50008', '50009', '50010', '50011', '50012', '50014', '50016', '50017', '50020', '50021', '50028', '66002', '66003', '66004', '66005', '66006', '66008', '66009', '66010', '66011', '66012', '66014', '66016', '66017', '66020', '66021', '66028']
        
        self.relationship_properties = {"element": "Import quantity", "element_code": "5607", "element_codes": ["5607", "5608", "5609", "5610", "5622", "5907", "5908", "5909", "5910", "5922", "50002", "50003", "50004", "50005", "50006", "50008", "50009", "50010", "50011", "50012", "50014", "50016", "50017", "50020", "50021", "50028", "66002", "66003", "66004", "66005", "66006", "66008", "66009", "66010", "66011", "66012", "66014", "66016", "66017", "66020", "66021", "66028"], "elements": true, "flow_direction": "bidirectional"}
    
    def get_migration_query(self) -> str:
        return load_sql("trade_crops_livestock_trades.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("trade_crops_livestock_trades_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("trade_crops_livestock_trades_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for trade_crops_livestock TRADES relationships"""
        logger.info(f"Starting trade_crops_livestock TRADES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 5607, 5608, 5609, 5610, 5622... (42 total)")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['5607', '5608', '5609', '5610', '5622', '5907', '5908', '5909', '5910', '5922', '50002', '50003', '50004', '50005', '50006', '50008', '50009', '50010', '50011', '50012', '50014', '50016', '50017', '50020', '50021', '50028', '66002', '66003', '66004', '66005', '66006', '66008', '66009', '66010', '66011', '66012', '66014', '66016', '66017', '66020', '66021', '66028'], 'element': 'Import quantity', 'element_code': '5607', 'elements': True, 'flow_direction': 'bidirectional'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} TRADES relationships from trade_crops_livestock")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ntrade_crops_livestock relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate trade_crops_livestock relationships: {e}")
            raise MigrationError(f"trade_crops_livestock relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass