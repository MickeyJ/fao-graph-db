"""Run food_balance_sheets_supplies migration"""
from .food_balance_sheets_supplies import FoodBalanceSheetsSuppliesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute food_balance_sheets_supplies migration"""
    try:
        migrator = FoodBalanceSheetsSuppliesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()