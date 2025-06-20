"""Run trade_crops_livestock_indicators_competes migration"""
from .trade_crops_livestock_indicators_competes import TradeCropsLivestockIndicatorsCompetesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute trade_crops_livestock_indicators_competes migration"""
    try:
        migrator = TradeCropsLivestockIndicatorsCompetesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()