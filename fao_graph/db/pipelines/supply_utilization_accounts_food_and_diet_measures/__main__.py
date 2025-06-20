"""Run supply_utilization_accounts_food_and_diet_measures migration"""
from .supply_utilization_accounts_food_and_diet_measures import SupplyUtilizationAccountsFoodAndDietMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute supply_utilization_accounts_food_and_diet_measures migration"""
    try:
        migrator = SupplyUtilizationAccountsFoodAndDietMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()