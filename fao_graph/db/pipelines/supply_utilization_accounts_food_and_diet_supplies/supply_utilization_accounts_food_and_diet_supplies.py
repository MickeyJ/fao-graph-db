# Template: relationship_migrator.py.jinja2
# Generated relationship migrator for supply_utilization_accounts_food_and_diet SUPPLIES relationships
from pathlib import Path
from sqlalchemy import text
from fao_graph.db.graph_migration_base import GraphMigrationBase
from fao_graph.db.database import get_session
from fao_graph.core.exceptions import MigrationError
from fao_graph.utils import load_sql
from fao_graph.logger import logger


class SupplyUtilizationAccountsFoodAndDietSuppliesMigrator(GraphMigrationBase):
    """Migrator for supply_utilization_accounts_food_and_diet SUPPLIES relationships"""
    
    def __init__(self):
        super().__init__("supply_utilization_accounts_food_and_diet", "relationship")
        self.relationship_type = "SUPPLIES"
        
        self.element_codes = ['6123', '6128', '6206', '6209']
        self.indicator_codes = ['4004', '4005', '4007', '4009', '4010', '4017', '4018', '4024', '4029', '4033', '4034', '4035', '4036', '4003', '4006', '4011', '4012', '4013', '4015', '4016', '4021', '4022', '4032', '4037', '4038']
        
        self.relationship_properties = {"indicator": "Protein supply", "indicator_code": "4004", "indicator_codes": ["4004", "4005", "4007", "4009", "4010", "4017", "4018", "4024", "4029", "4033", "4034", "4035", "4036", "4003", "4006", "4011", "4012", "4013", "4015", "4016", "4021", "4022", "4032", "4037", "4038"], "indicators": true, "nutrient_type": "protein"}
    
    def get_migration_query(self) -> str:
        return load_sql("supply_utilization_accounts_food_and_diet_supplies.cypher.sql", Path(__file__).parent)
    
    def get_index_queries(self) -> str:
        return load_sql("supply_utilization_accounts_food_and_diet_supplies_indexes.sql", Path(__file__).parent)
    
    def get_verification_query(self) -> str:
        return load_sql("supply_utilization_accounts_food_and_diet_supplies_verify.cypher.sql", Path(__file__).parent)
    
    def migrate(self, start_offset: int = 0, mode: str = "create") -> None:
        """Execute the migration for supply_utilization_accounts_food_and_diet SUPPLIES relationships"""
        logger.info(f"Starting supply_utilization_accounts_food_and_diet SUPPLIES relationship migration...")
        
        logger.info(f"  Filtering on element codes: 6123, 6128, 6206, 6209")
        logger.info(f"  Filtering on indicator codes: 4004, 4005, 4007, 4009, 4010... (25 total)")
        
        logger.info(f"  Relationship type properties: {'indicator_codes': ['4004', '4005', '4007', '4009', '4010', '4017', '4018', '4024', '4029', '4033', '4034', '4035', '4036', '4003', '4006', '4011', '4012', '4013', '4015', '4016', '4021', '4022', '4032', '4037', '4038'], 'indicator': 'Protein supply', 'indicator_code': '4004', 'indicators': True, 'nutrient_type': 'protein'}")
        
        try:
            # Execute the main migration
            with get_session() as session:
                query = self.get_migration_query()
                result = session.execute(text(query)).fetchall()
                self.created = len(result)
                logger.info(f"Created {self.created} SUPPLIES relationships from supply_utilization_accounts_food_and_diet")
            
            # Create indexes
            self.create_indexes()
                    
        except KeyboardInterrupt:
            logger.warning(f"\nsupply_utilization_accounts_food_and_diet relationship migration interrupted")
            raise
        except Exception as e:
            logger.error(f"Failed to migrate supply_utilization_accounts_food_and_diet relationships: {e}")
            raise MigrationError(f"supply_utilization_accounts_food_and_diet relationship migration failed: {e}") from e
    
    def create(self, records):
        # Not used when overriding migrate()
        pass
    
    def update(self, records):
        # Not used when overriding migrate()
        pass