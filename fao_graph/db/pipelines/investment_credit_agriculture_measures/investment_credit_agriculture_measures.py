# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for investment_credit_agriculture MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class InvestmentCreditAgricultureMeasuresMigrator(GraphMigrationBase):
    """Migrator for investment_credit_agriculture MEASURES relationships"""
    
    def __init__(self):
        super().__init__("investment_credit_agriculture", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['6110', '6184', '6224', '6225']
        self.elements = ['Value US$', 'Value US$, 2015 prices', 'Value Standard Local Currency', 'Value Standard Local Currency, 2015 prices']
        self.relationship_properties = {"category": "financial", "element": "Value Standard Local Currency, 2015 prices", "element_code": "6225", "flow_type": "credit"}
    
    def get_migration_query(self) -> str:
        return load_sql("investment_credit_agriculture_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("investment_credit_agriculture_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("investment_credit_agriculture_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for investment_credit_agriculture MEASURES relationships"""
        logger.info(f"Starting investment_credit_agriculture MEASURES relationship migration...")
        logger.info(f"  Elements: Value US$, Value US$, 2015 prices, Value Standard Local Currency, Value Standard Local Currency, 2015 prices")
        logger.info(f"  Properties: {'category': 'financial', 'flow_type': 'credit', 'element_code': '6225', 'element': 'Value Standard Local Currency, 2015 prices'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from investment_credit_agriculture")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ninvestment_credit_agriculture relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate investment_credit_agriculture relationships: {e}")
            raise MigrationError(f"investment_credit_agriculture relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass