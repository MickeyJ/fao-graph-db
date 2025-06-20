"""Run food_balance_sheets_trades migration"""
from .food_balance_sheets_trades import FoodBalanceSheetsTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute food_balance_sheets_trades migration"""
    try:
        migrator = FoodBalanceSheetsTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()