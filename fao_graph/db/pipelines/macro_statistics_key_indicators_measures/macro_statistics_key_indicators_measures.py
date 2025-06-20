# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for macro_statistics_key_indicators MEASURES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class MacroStatisticsKeyIndicatorsMeasuresMigrator(GraphMigrationBase):
    """Migrator for macro_statistics_key_indicators MEASURES relationships"""
    
    def __init__(self):
        super().__init__("macro_statistics_key_indicators", "relationship")
        self.relationship_type = "MEASURES"
        self.element_codes = ['6103', '6110', '6119', '6129', '61290', '6143', '61550', '61570', '6163', '61810', '6182', '61820', '6184', '6185', '61860', '6187', '61890', '61900', '6224', '6225']
        self.elements = ['Share of GDP US$', 'Value US$', 'Value US$ per capita', 'Annual growth US$', 'Annual growth US$ per capita', 'Share of Value Added (Total Manufacturing) US$', 'Annual growth Standard Local Currency', 'Share of GDP Standard Local Currency', 'Ratio of Value Added (Agriculture, Forestry and Fishing) US$', 'Annual growth Standard Local Currency, 2015 prices', 'Annual growth US$, 2015 prices', 'Annual growth US$ per capita, 2015 prices', 'Value US$, 2015 prices', 'Value US$ per capita, 2015 prices', 'Share of GDP Standard Local Currency, 2015 prices', 'Share of GDP US$, 2015 prices', 'Ratio of Value Added (Agriculture, Forestry and Fishing) Standard Local Currency', 'Share of Value Added (Total Manufacturing) Standard Local Currency', 'Value Standard Local Currency', 'Value Standard Local Currency, 2015 prices']
        self.relationship_properties = {"category": "general", "element": "Value Standard Local Currency, 2015 prices", "element_code": "6225", "measure": "value"}
    
    def get_migration_query(self) -> str:
        return load_sql("macro_statistics_key_indicators_measures.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("macro_statistics_key_indicators_measures_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("macro_statistics_key_indicators_measures_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for macro_statistics_key_indicators MEASURES relationships"""
        logger.info(f"Starting macro_statistics_key_indicators MEASURES relationship migration...")
        logger.info(f"  Elements: Share of GDP US$, Value US$, Value US$ per capita, Annual growth US$, Annual growth US$ per capita, Share of Value Added (Total Manufacturing) US$, Annual growth Standard Local Currency, Share of GDP Standard Local Currency, Ratio of Value Added (Agriculture, Forestry and Fishing) US$, Annual growth Standard Local Currency, 2015 prices, Annual growth US$, 2015 prices, Annual growth US$ per capita, 2015 prices, Value US$, 2015 prices, Value US$ per capita, 2015 prices, Share of GDP Standard Local Currency, 2015 prices, Share of GDP US$, 2015 prices, Ratio of Value Added (Agriculture, Forestry and Fishing) Standard Local Currency, Share of Value Added (Total Manufacturing) Standard Local Currency, Value Standard Local Currency, Value Standard Local Currency, 2015 prices")
        logger.info(f"  Properties: {'category': 'general', 'measure': 'value', 'element_code': '6225', 'element': 'Value Standard Local Currency, 2015 prices'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} MEASURES relationships from macro_statistics_key_indicators")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nmacro_statistics_key_indicators relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate macro_statistics_key_indicators relationships: {e}")
            raise MigrationError(f"macro_statistics_key_indicators relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass