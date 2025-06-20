"""Run macro_statistics_key_indicators_measures migration"""
from .macro_statistics_key_indicators_measures import MacroStatisticsKeyIndicatorsMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute macro_statistics_key_indicators_measures migration"""
    try:
        migrator = MacroStatisticsKeyIndicatorsMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()