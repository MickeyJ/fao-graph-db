"""Run commodity_balances_non_food_2013_old_methodology_trades migration"""
from .commodity_balances_non_food_2013_old_methodology_trades import CommodityBalancesNonFood2013OldMethodologyTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute commodity_balances_non_food_2013_old_methodology_trades migration"""
    try:
        migrator = CommodityBalancesNonFood2013OldMethodologyTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()