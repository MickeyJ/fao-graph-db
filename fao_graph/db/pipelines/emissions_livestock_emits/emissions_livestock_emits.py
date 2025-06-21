# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for emissions_livestock EMITS relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class EmissionsLivestockEmitsMigrator(GraphMigrationBase):
    """Migrator for emissions_livestock EMITS relationships"""
    
    def __init__(self):
        super().__init__("emissions_livestock", "relationship")
        self.relationship_type = "EMITS"
        
        self.element_codes = ['72254', '72256', '72300', '72301', '72306', '72340', '72341', '72346', '72360', '723601', '723602', '72361', '723611', '723612', '72366', '72431', '72441']
        
        self.relationship_properties = {"element": "Enteric fermentation (Emissions CH4)", "element_code": "72254", "element_codes": ["72254", "72256", "72300", "72301", "72306", "72340", "72341", "72346", "72360", "723601", "723602", "72361", "723611", "723612", "72366", "72431", "72441"], "elements": true, "gas_type": "CH4"}
    
    def get_migration_query(self) -> str:
        return load_sql("emissions_livestock_emits.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("emissions_livestock_emits_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("emissions_livestock_emits_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for emissions_livestock EMITS relationships"""
        logger.info(f"Starting emissions_livestock EMITS relationship migration...")
        
        logger.info(f"  Filtering on element codes: 72254, 72256, 72300, 72301, 72306... (17 total)")
        
        logger.info(f"  Relationship type properties: {'element_codes': ['72254', '72256', '72300', '72301', '72306', '72340', '72341', '72346', '72360', '723601', '723602', '72361', '723611', '723612', '72366', '72431', '72441'], 'element': 'Enteric fermentation (Emissions CH4)', 'element_code': '72254', 'elements': True, 'gas_type': 'CH4'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} EMITS relationships from emissions_livestock")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nemissions_livestock relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate emissions_livestock relationships: {e}")
            raise MigrationError(f"emissions_livestock relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass