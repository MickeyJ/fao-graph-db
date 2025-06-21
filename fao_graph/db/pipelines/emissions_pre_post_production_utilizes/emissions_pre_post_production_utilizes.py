# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for emissions_pre_post_production UTILIZES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EmissionsPrePostProductionUtilizesMigrator(GraphMigrationBase):
    """Migrator for emissions_pre_post_production UTILIZES relationships"""
    
    def __init__(self):
        super().__init__("emissions_pre_post_production", "relationship")
        self.relationship_type = "UTILIZES"
        
        self.element_codes = ['723116', '723117', '723118', '723119', '723120']
        
        self.relationship_properties = {"element": "Energy Use (Natural Gas, including LNG)", "element_code": "723116", "element_codes": ["723116", "723117", "723118", "723119", "723120"], "elements": true}
    
    def get_migration_query(self) -> str:
        return load_sql("emissions_pre_post_production_utilizes.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("emissions_pre_post_production_utilizes_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("emissions_pre_post_production_utilizes_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for emissions_pre_post_production UTILIZES relationships"""
        logger.info(f"Starting emissions_pre_post_production UTILIZES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 723116, 723117, 723118, 723119, 723120")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['723116', '723117', '723118', '723119', '723120'], 'element': 'Energy Use (Natural Gas, including LNG)', 'element_code': '723116', 'elements': True}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} UTILIZES relationships from emissions_pre_post_production")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nemissions_pre_post_production relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate emissions_pre_post_production relationships: {e}")
            raise MigrationError(f"emissions_pre_post_production relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass