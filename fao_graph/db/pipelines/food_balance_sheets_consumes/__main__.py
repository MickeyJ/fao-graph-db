"""Run food_balance_sheets_consumes migration"""
from .food_balance_sheets_consumes import FoodBalanceSheetsConsumesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute food_balance_sheets_consumes migration"""
    try:
        migrator = FoodBalanceSheetsConsumesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()