"""Run sdg_bulk_downloads_measures migration"""
from .sdg_bulk_downloads_measures import SdgBulkDownloadsMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute sdg_bulk_downloads_measures migration"""
    try:
        migrator = SdgBulkDownloadsMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()