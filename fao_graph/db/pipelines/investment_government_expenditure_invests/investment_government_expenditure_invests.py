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
        self.element_codes = ['61060', '6111', '6131', '6197']
        self.elements = ['SDG 2.a.1: Agriculture value added share of GDP', 'Share of Total Expenditure', 'SDG 2.a.1: Agriculture share of Government Expenditure', 'SDG 2.a.1: Agriculture Orientation Index (AOI) for Government Expenditure']
        self.relationship_properties = {"currency": "local", "element": "SDG 2.a.1: Agriculture Orientation Index (AOI) for Government Expenditure", "element_code": "6197", "measure": "agriculture_orientation_index"}
    
    def get_migration_query(self) -> str:
        return load_sql("investment_government_expenditure_invests.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("investment_government_expenditure_invests_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("investment_government_expenditure_invests_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for investment_government_expenditure INVESTS relationships"""
        logger.info(f"Starting investment_government_expenditure INVESTS relationship migration...")
        logger.info(f"  Elements: SDG 2.a.1: Agriculture value added share of GDP, Share of Total Expenditure, SDG 2.a.1: Agriculture share of Government Expenditure, SDG 2.a.1: Agriculture Orientation Index (AOI) for Government Expenditure")
        logger.info(f"  Properties: {'measure': 'agriculture_orientation_index', 'currency': 'local', 'element_code': '6197', 'element': 'SDG 2.a.1: Agriculture Orientation Index (AOI) for Government Expenditure'}")
        
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