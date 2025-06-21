# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for value_shares_industry_primary_factors TRADES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ValueSharesIndustryPrimaryFactorsTradesMigrator(GraphMigrationBase):
    """Migrator for value_shares_industry_primary_factors TRADES relationships"""
    
    def __init__(self):
        super().__init__("value_shares_industry_primary_factors", "relationship")
        self.relationship_type = "TRADES"
        
        self.factor_codes = ['22125']
        
        self.relationship_properties = {"flow_direction": "unspecified", "industries": true, "industry": "Wholesale and retail trade", "industry_code": "22119", "industry_codes": ["22119"]}
    
    def get_migration_query(self) -> str:
        return load_sql("value_shares_industry_primary_factors_trades.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("value_shares_industry_primary_factors_trades_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("value_shares_industry_primary_factors_trades_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for value_shares_industry_primary_factors TRADES relationships"""
        logger.info(f"Starting value_shares_industry_primary_factors TRADES relationship migration...")
        
        logger.info(f"  Filtering on factor codes: 22125")
        
        logger.info(f"  Relationship type properties: {'industry_codes': ['22119'], 'industry': 'Wholesale and retail trade', 'industry_code': '22119', 'industries': True, 'flow_direction': 'unspecified'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} TRADES relationships from value_shares_industry_primary_factors")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nvalue_shares_industry_primary_factors relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate value_shares_industry_primary_factors relationships: {e}")
            raise MigrationError(f"value_shares_industry_primary_factors relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass