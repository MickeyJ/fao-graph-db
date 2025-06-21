# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for commodity_balances_non_food_2013_old_methodology PRODUCES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class CommodityBalancesNonFood2013OldMethodologyProducesMigrator(GraphMigrationBase):
    """Migrator for commodity_balances_non_food_2013_old_methodology PRODUCES relationships"""
    
    def __init__(self):
        super().__init__("commodity_balances_non_food_2013_old_methodology", "relationship")
        self.relationship_type = "PRODUCES"
        
        self.element_codes = ['5510']
        
        self.relationship_properties = {"element": "Production", "element_code": "5510", "element_codes": ["5510"], "elements": true}
    
    def get_migration_query(self) -> str:
        return load_sql("commodity_balances_non_food_2013_old_methodology_produces.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("commodity_balances_non_food_2013_old_methodology_produces_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("commodity_balances_non_food_2013_old_methodology_produces_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for commodity_balances_non_food_2013_old_methodology PRODUCES relationships"""
        logger.info(f"Starting commodity_balances_non_food_2013_old_methodology PRODUCES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 5510")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['5510'], 'element': 'Production', 'element_code': '5510', 'elements': True}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} PRODUCES relationships from commodity_balances_non_food_2013_old_methodology")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\ncommodity_balances_non_food_2013_old_methodology relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate commodity_balances_non_food_2013_old_methodology relationships: {e}")
            raise MigrationError(f"commodity_balances_non_food_2013_old_methodology relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass