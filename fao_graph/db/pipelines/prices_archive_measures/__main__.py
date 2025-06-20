"""Run prices_archive_measures migration"""
from .prices_archive_measures import PricesArchiveMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute prices_archive_measures migration"""
    try:
        migrator = PricesArchiveMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()