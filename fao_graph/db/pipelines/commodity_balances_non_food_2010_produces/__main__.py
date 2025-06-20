"""Run commodity_balances_non_food_2010_produces migration"""
from .commodity_balances_non_food_2010_produces import CommodityBalancesNonFood2010ProducesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute commodity_balances_non_food_2010_produces migration"""
    try:
        migrator = CommodityBalancesNonFood2010ProducesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()