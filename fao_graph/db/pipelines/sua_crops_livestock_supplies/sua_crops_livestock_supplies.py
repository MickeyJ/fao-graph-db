# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for sua_crops_livestock SUPPLIES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class SuaCropsLivestockSuppliesMigrator(GraphMigrationBase):
    """Migrator for sua_crops_livestock SUPPLIES relationships"""
    
    def __init__(self):
        super().__init__("sua_crops_livestock", "relationship")
        self.relationship_type = "SUPPLIES"
        self.element_codes = ['674', '684']
        self.elements = ['Protein supply quantity (g/capita/day)', 'Fat supply quantity (g/capita/day)']
        self.relationship_properties = {"element": "Fat supply quantity (g/capita/day)", "element_code": "684", "measure": "quantity", "nutrient": "fat", "unit": "g/capita/day"}
    
    def get_migration_query(self) -> str:
        return load_sql("sua_crops_livestock_supplies.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("sua_crops_livestock_supplies_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("sua_crops_livestock_supplies_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for sua_crops_livestock SUPPLIES relationships"""
        logger.info(f"Starting sua_crops_livestock SUPPLIES relationship migration...")
        logger.info(f"  Elements: Protein supply quantity (g/capita/day), Fat supply quantity (g/capita/day)")
        logger.info(f"  Properties: {'nutrient': 'fat', 'measure': 'quantity', 'unit': 'g/capita/day', 'element_code': '684', 'element': 'Fat supply quantity (g/capita/day)'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} SUPPLIES relationships from sua_crops_livestock")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nsua_crops_livestock relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate sua_crops_livestock relationships: {e}")
            raise MigrationError(f"sua_crops_livestock relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass