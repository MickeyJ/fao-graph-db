# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for investment_capital_stock INVESTS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class InvestmentCapitalStockInvestsMigrator(GraphMigrationBase):
    """Migrator for investment_capital_stock INVESTS relationships"""
    
    def __init__(self):
        super().__init__("investment_capital_stock", "relationship")
        self.relationship_type = "INVESTS"
        
        self.element_codes = ['61391', '61392', '61393', '61394', '6110', '61120', '6159', '6184', '6193', '61940', '6224', '6225']
        
        self.relationship_properties = {"element": "Share of Gross Fixed Capital Formation US$", "element_code": "61391", "element_codes": ["61391", "61392", "61393", "61394", "6110", "61120", "6159", "6184", "6193", "61940", "6224", "6225"]}
    
    def get_migration_query(self) -> str:
        return load_sql("investment_capital_stock_invests.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("investment_capital_stock_invests_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("investment_capital_stock_invests_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for investment_capital_stock INVESTS relationships"""
        logger.info(f"Starting investment_capital_stock INVESTS relationship migration...")
        
        logger.info(f"  Filtering on element codes: 61391, 61392, 61393, 61394, 6110... (12 total)")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['61391', '61392', '61393', '61394', '6110', '61120', '6159', '6184', '6193', '61940', '6224', '6225'], 'element': 'Share of Gross Fixed Capital Formation US$', 'element_code': '61391'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} INVESTS relationships from investment_capital_stock")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ninvestment_capital_stock relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate investment_capital_stock relationships: {e}")
            raise MigrationError(f"investment_capital_stock relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass