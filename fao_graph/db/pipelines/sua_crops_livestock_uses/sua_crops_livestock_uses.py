# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for sua_crops_livestock USES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class SuaCropsLivestockUsesMigrator(GraphMigrationBase):
    """Migrator for sua_crops_livestock USES relationships"""
    
    def __init__(self):
        super().__init__("sua_crops_livestock", "relationship")
        self.relationship_type = "USES"
        self.element_codes = ['5141', '5165', '5520', '664', '665']
        self.elements = ['Food supply quantity (tonnes)', 'Other uses (non-food)', 'Feed', 'Food supply (kcal/capita/day)', 'Food supply quantity (g/capita/day)']
        self.relationship_properties = {"element": "Food supply quantity (g/capita/day)", "element_code": "665", "purpose": "food", "resource": "food_supply"}
    
    def get_migration_query(self) -> str:
        return load_sql("sua_crops_livestock_uses.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("sua_crops_livestock_uses_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("sua_crops_livestock_uses_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for sua_crops_livestock USES relationships"""
        logger.info(f"Starting sua_crops_livestock USES relationship migration...")
        logger.info(f"  Elements: Food supply quantity (tonnes), Other uses (non-food), Feed, Food supply (kcal/capita/day), Food supply quantity (g/capita/day)")
        logger.info(f"  Properties: {'resource': 'food_supply', 'purpose': 'food', 'element_code': '665', 'element': 'Food supply quantity (g/capita/day)'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} USES relationships from sua_crops_livestock")
            
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