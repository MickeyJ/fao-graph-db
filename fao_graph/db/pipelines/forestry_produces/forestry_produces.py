# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for forestry PRODUCES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class ForestryProducesMigrator(GraphMigrationBase):
    """Migrator for forestry PRODUCES relationships"""
    
    def __init__(self):
        super().__init__("forestry", "relationship")
        self.relationship_type = "PRODUCES"
        
        self.element_codes = ['5510', '5516']
        
        self.relationship_properties = {"element": "Production", "element_code": "5510", "element_codes": ["5510", "5516"]}
    
    def get_migration_query(self) -> str:
        return load_sql("forestry_produces.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("forestry_produces_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("forestry_produces_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for forestry PRODUCES relationships"""
        logger.info(f"Starting forestry PRODUCES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 5510, 5516")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['5510', '5516'], 'element': 'Production', 'element_code': '5510'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} PRODUCES relationships from forestry")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nforestry relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate forestry relationships: {e}")
            raise MigrationError(f"forestry relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass