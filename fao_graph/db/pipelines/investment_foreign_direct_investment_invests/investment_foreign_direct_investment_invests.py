# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for investment_foreign_direct_investment INVESTS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class InvestmentForeignDirectInvestmentInvestsMigrator(GraphMigrationBase):
    """Migrator for investment_foreign_direct_investment INVESTS relationships"""
    
    def __init__(self):
        super().__init__("investment_foreign_direct_investment", "relationship")
        self.relationship_type = "INVESTS"
        self.element_codes = ['61410', '61420']
        self.elements = ['Share of Total FDI inflows US$, 2015 prices', 'Share of Total FDI outflows US$, 2015 prices']
        self.relationship_properties = {"currency": "USD", "element": "Share of Total FDI outflows US$, 2015 prices", "element_code": "61420", "measure": "share_of_investment"}
    
    def get_migration_query(self) -> str:
        return load_sql("investment_foreign_direct_investment_invests.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("investment_foreign_direct_investment_invests_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("investment_foreign_direct_investment_invests_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for investment_foreign_direct_investment INVESTS relationships"""
        logger.info(f"Starting investment_foreign_direct_investment INVESTS relationship migration...")
        logger.info(f"  Elements: Share of Total FDI inflows US$, 2015 prices, Share of Total FDI outflows US$, 2015 prices")
        logger.info(f"  Properties: {'measure': 'share_of_investment', 'currency': 'USD', 'element_code': '61420', 'element': 'Share of Total FDI outflows US$, 2015 prices'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} INVESTS relationships from investment_foreign_direct_investment")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ninvestment_foreign_direct_investment relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate investment_foreign_direct_investment relationships: {e}")
            raise MigrationError(f"investment_foreign_direct_investment relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass