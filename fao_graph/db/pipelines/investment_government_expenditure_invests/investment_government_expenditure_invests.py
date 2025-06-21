# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for investment_government_expenditure INVESTS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class InvestmentGovernmentExpenditureInvestsMigrator(GraphMigrationBase):
    """Migrator for investment_government_expenditure INVESTS relationships"""
    
    def __init__(self):
        super().__init__("investment_government_expenditure", "relationship")
        self.relationship_type = "INVESTS"
        
        self.element_codes = ['6131', '6197', '6111', '61060', '6110', '6184', '6224']
        
        self.relationship_properties = {"element": "SDG 2.a.1: Agriculture share of Government Expenditure", "element_code": "6131", "element_codes": ["6131", "6197", "6111", "61060", "6110", "6184", "6224"], "elements": true}
    
    def get_migration_query(self) -> str:
        return load_sql("investment_government_expenditure_invests.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("investment_government_expenditure_invests_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("investment_government_expenditure_invests_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for investment_government_expenditure INVESTS relationships"""
        logger.info(f"Starting investment_government_expenditure INVESTS relationship migration...")
        
        logger.info(f"  Filtering on element codes: 6131, 6197, 6111, 61060, 6110... (7 total)")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['6131', '6197', '6111', '61060', '6110', '6184', '6224'], 'element': 'SDG 2.a.1: Agriculture share of Government Expenditure', 'element_code': '6131', 'elements': True}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} INVESTS relationships from investment_government_expenditure")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ninvestment_government_expenditure relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate investment_government_expenditure relationships: {e}")
            raise MigrationError(f"investment_government_expenditure relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass