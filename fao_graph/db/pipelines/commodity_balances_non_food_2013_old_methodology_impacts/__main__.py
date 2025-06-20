"""Run commodity_balances_non_food_2013_old_methodology_impacts migration"""
from .commodity_balances_non_food_2013_old_methodology_impacts import CommodityBalancesNonFood2013OldMethodologyImpactsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute commodity_balances_non_food_2013_old_methodology_impacts migration"""
    try:
        migrator = CommodityBalancesNonFood2013OldMethodologyImpactsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()