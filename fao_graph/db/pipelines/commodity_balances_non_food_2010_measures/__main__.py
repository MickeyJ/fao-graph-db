"""Run commodity_balances_non_food_2010_measures migration"""
from .commodity_balances_non_food_2010_measures import CommodityBalancesNonFood2010MeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute commodity_balances_non_food_2010_measures migration"""
    try:
        migrator = CommodityBalancesNonFood2010MeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()