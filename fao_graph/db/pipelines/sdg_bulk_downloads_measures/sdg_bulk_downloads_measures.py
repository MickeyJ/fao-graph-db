# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for sdg_bulk_downloads MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class SdgBulkDownloadsMeasuresMigrator(GraphMigrationBase):
    """Migrator for sdg_bulk_downloads MEASURES relationships"""
    
    def __init__(self):
        super().__init__("sdg_bulk_downloads", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['6121', '61211', '61212', '6125', '6132', '6173', '6174', '61741', '6176', '6177', '6178', '6199', '61991', '61992', '6204', '6241']
        self.elements = ['Value', 'Confidence interval: Lower bound', 'Confidence interval: Upper bound', 'Value', 'Value', 'Value', 'Value (2017 constant prices)', 'Value (2017 constant prices)', 'Value', 'Value', 'Value', 'Value', 'Confidence interval: Lower bound', 'Confidence interval: Upper bound', 'Value', 'Value']
        self.relationship_properties = {"category": "general", "element": "Value", "element_code": "6241", "measure": "value"}
    
    def get_migration_query(self) -> str:
        return load_sql("sdg_bulk_downloads_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("sdg_bulk_downloads_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("sdg_bulk_downloads_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for sdg_bulk_downloads MEASURES relationships"""
        logger.info(f"Starting sdg_bulk_downloads MEASURES relationship migration...")
        logger.info(f"  Elements: Value, Confidence interval: Lower bound, Confidence interval: Upper bound, Value, Value, Value, Value (2017 constant prices), Value (2017 constant prices), Value, Value, Value, Value, Confidence interval: Lower bound, Confidence interval: Upper bound, Value, Value")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'value', 'element_code': '6241', 'element': 'Value'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from sdg_bulk_downloads")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nsdg_bulk_downloads relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate sdg_bulk_downloads relationships: {e}")
            raise MigrationError(f"sdg_bulk_downloads relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass