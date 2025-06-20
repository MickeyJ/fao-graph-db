# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for value_of_production PRODUCES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ValueOfProductionProducesMigrator(GraphMigrationBase):
    """Migrator for value_of_production PRODUCES relationships"""
    
    def __init__(self):
        super().__init__("value_of_production", "relationship")
        self.relationship_type = "PRODUCES"
        
        self.element_codes = ['152', '55', '56', '57', '58']
        
        self.relationship_properties = {"element": "Gross Production Value (constant 2014-2016 thousand I$)", "element_code": "152", "element_codes": ["152", "55", "56", "57", "58"], "elements": true}
    
    def get_migration_query(self) -> str:
        return load_sql("value_of_production_produces.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("value_of_production_produces_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("value_of_production_produces_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for value_of_production PRODUCES relationships"""
        logger.info(f"Starting value_of_production PRODUCES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 152, 55, 56, 57, 58")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['152', '55', '56', '57', '58'], 'element': 'Gross Production Value (constant 2014-2016 thousand I$)', 'element_code': '152', 'elements': True}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} PRODUCES relationships from value_of_production")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nvalue_of_production relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate value_of_production relationships: {e}")
            raise MigrationError(f"value_of_production relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass