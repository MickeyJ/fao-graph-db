"""Run food_balance_sheets_historic_supplies migration"""
from .food_balance_sheets_historic_supplies import FoodBalanceSheetsHistoricSuppliesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute food_balance_sheets_historic_supplies migration"""
    try:
        migrator = FoodBalanceSheetsHistoricSuppliesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()