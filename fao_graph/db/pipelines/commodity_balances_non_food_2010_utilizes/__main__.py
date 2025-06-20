"""Run commodity_balances_non_food_2010_utilizes migration"""
from .commodity_balances_non_food_2010_utilizes import CommodityBalancesNonFood2010UtilizesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute commodity_balances_non_food_2010_utilizes migration"""
    try:
        migrator = CommodityBalancesNonFood2010UtilizesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()