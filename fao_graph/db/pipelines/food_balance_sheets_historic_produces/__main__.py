"""Run food_balance_sheets_historic_produces migration"""
from .food_balance_sheets_historic_produces import FoodBalanceSheetsHistoricProducesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute food_balance_sheets_historic_produces migration"""
    try:
        migrator = FoodBalanceSheetsHistoricProducesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()