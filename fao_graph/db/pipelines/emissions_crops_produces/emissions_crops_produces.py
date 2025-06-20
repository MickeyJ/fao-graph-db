# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for emissions_crops PRODUCES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EmissionsCropsProducesMigrator(GraphMigrationBase):
    """Migrator for emissions_crops PRODUCES relationships"""
    
    def __init__(self):
        super().__init__("emissions_crops", "relationship")
        self.relationship_type = "PRODUCES"
        
        self.element_codes = ['5312', '72392', '7245']
        
        self.relationship_properties = {"element": "Area harvested", "element_code": "5312", "element_codes": ["5312", "72392", "7245"]}
    
    def get_migration_query(self) -> str:
        return load_sql("emissions_crops_produces.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("emissions_crops_produces_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("emissions_crops_produces_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for emissions_crops PRODUCES relationships"""
        logger.info(f"Starting emissions_crops PRODUCES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 5312, 72392, 7245")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['5312', '72392', '7245'], 'element': 'Area harvested', 'element_code': '5312'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} PRODUCES relationships from emissions_crops")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nemissions_crops relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate emissions_crops relationships: {e}")
            raise MigrationError(f"emissions_crops relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass