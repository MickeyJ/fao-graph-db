"""Run supply_utilization_accounts_food_and_diet_supplies migration"""
from .supply_utilization_accounts_food_and_diet_supplies import SupplyUtilizationAccountsFoodAndDietSuppliesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute supply_utilization_accounts_food_and_diet_supplies migration"""
    try:
        migrator = SupplyUtilizationAccountsFoodAndDietSuppliesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()