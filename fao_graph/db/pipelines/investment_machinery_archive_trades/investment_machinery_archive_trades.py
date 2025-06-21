# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for investment_machinery_archive TRADES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class InvestmentMachineryArchiveTradesMigrator(GraphMigrationBase):
    """Migrator for investment_machinery_archive TRADES relationships"""
    
    def __init__(self):
        super().__init__("investment_machinery_archive", "relationship")
        self.relationship_type = "TRADES"
        
        self.element_codes = ['5607', '5622', '5907', '5922']
        
        self.relationship_properties = {"element": "Import Quantity", "element_code": "5607", "element_codes": ["5607", "5622", "5907", "5922"], "elements": true, "flow_direction": "bidirectional"}
    
    def get_migration_query(self) -> str:
        return load_sql("investment_machinery_archive_trades.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("investment_machinery_archive_trades_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("investment_machinery_archive_trades_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for investment_machinery_archive TRADES relationships"""
        logger.info(f"Starting investment_machinery_archive TRADES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 5607, 5622, 5907, 5922")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['5607', '5622', '5907', '5922'], 'element': 'Import Quantity', 'element_code': '5607', 'elements': True, 'flow_direction': 'bidirectional'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} TRADES relationships from investment_machinery_archive")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ninvestment_machinery_archive relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate investment_machinery_archive relationships: {e}")
            raise MigrationError(f"investment_machinery_archive relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass