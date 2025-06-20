"""Run food_balance_sheets_historic_uses migration"""
from .food_balance_sheets_historic_uses import FoodBalanceSheetsHistoricUsesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute food_balance_sheets_historic_uses migration"""
    try:
        migrator = FoodBalanceSheetsHistoricUsesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()