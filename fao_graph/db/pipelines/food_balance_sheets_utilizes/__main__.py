"""Run food_balance_sheets_utilizes migration"""
from .food_balance_sheets_utilizes import FoodBalanceSheetsUtilizesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute food_balance_sheets_utilizes migration"""
    try:
        migrator = FoodBalanceSheetsUtilizesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()