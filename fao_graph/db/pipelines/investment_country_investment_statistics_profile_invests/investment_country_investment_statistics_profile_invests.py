# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for investment_country_investment_statistics_profile INVESTS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class InvestmentCountryInvestmentStatisticsProfileInvestsMigrator(GraphMigrationBase):
    """Migrator for investment_country_investment_statistics_profile INVESTS relationships"""
    
    def __init__(self):
        super().__init__("investment_country_investment_statistics_profile", "relationship")
        self.relationship_type = "INVESTS"
        self.element_codes = ['6139', '61390', '6159', '6192', '6193']
        self.elements = ['Share of Total US$', 'Share of Total US$, 2015 prices', 'Agriculture orientation index US$', 'Share of Value Added US$, 2015 prices', 'Agriculture orientation index US$, 2015 prices']
        self.relationship_properties = {"currency": "USD", "element": "Agriculture orientation index US$, 2015 prices", "element_code": "6193", "measure": "agriculture_orientation_index"}
    
    def get_migration_query(self) -> str:
        return load_sql("investment_country_investment_statistics_profile_invests.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("investment_country_investment_statistics_profile_invests_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("investment_country_investment_statistics_profile_invests_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for investment_country_investment_statistics_profile INVESTS relationships"""
        logger.info(f"Starting investment_country_investment_statistics_profile INVESTS relationship migration...")
        logger.info(f"  Elements: Share of Total US$, Share of Total US$, 2015 prices, Agriculture orientation index US$, Share of Value Added US$, 2015 prices, Agriculture orientation index US$, 2015 prices")
        logger.info(f"  Properties: {'measure': 'agriculture_orientation_index', 'currency': 'USD', 'element_code': '6193', 'element': 'Agriculture orientation index US$, 2015 prices'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} INVESTS relationships from investment_country_investment_statistics_profile")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ninvestment_country_investment_statistics_profile relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate investment_country_investment_statistics_profile relationships: {e}")
            raise MigrationError(f"investment_country_investment_statistics_profile relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass