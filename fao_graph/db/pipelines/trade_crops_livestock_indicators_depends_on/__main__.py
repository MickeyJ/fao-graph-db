"""Run trade_crops_livestock_indicators_depends_on migration"""
from .trade_crops_livestock_indicators_depends_on import TradeCropsLivestockIndicatorsDepends_OnMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute trade_crops_livestock_indicators_depends_on migration"""
    try:
        migrator = TradeCropsLivestockIndicatorsDepends_OnMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()