"""Run prices_measures migration"""
from .prices_measures import PricesMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute prices_measures migration"""
    try:
        migrator = PricesMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()