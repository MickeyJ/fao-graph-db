# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for investment_foreign_direct_investment MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class InvestmentForeignDirectInvestmentMeasuresMigrator(GraphMigrationBase):
    """Migrator for investment_foreign_direct_investment MEASURES relationships"""
    
    def __init__(self):
        super().__init__("investment_foreign_direct_investment", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['5110']
        self.elements = ['Value']
    
    def get_migration_query(self) -> str:
        return load_sql("investment_foreign_direct_investment_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("investment_foreign_direct_investment_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("investment_foreign_direct_investment_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for investment_foreign_direct_investment MEASURES relationships"""
        logger.info(f"Starting investment_foreign_direct_investment MEASURES relationship migration...")
        logger.info(f"  Elements: Value")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                
                # Add source_table property for tracking
                query = query.replace(
                    "CREATE (source)-[r:MEASURES {",
                    "CREATE (source)-[r:MEASURES {source_dataset: 'investment_foreign_direct_investment', "
                )
                
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from investment_foreign_direct_investment")
            
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