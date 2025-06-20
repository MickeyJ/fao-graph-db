"""Run commodity_balances_non_food_2013_old_methodology_consumes migration"""
from .commodity_balances_non_food_2013_old_methodology_consumes import CommodityBalancesNonFood2013OldMethodologyConsumesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute commodity_balances_non_food_2013_old_methodology_consumes migration"""
    try:
        migrator = CommodityBalancesNonFood2013OldMethodologyConsumesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()