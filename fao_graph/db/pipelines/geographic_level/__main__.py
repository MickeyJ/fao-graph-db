"""Run geographic_level migration"""
from .geographic_level import GeographicLevelMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute geographic_level migration"""
    try:
        migrator = GeographicLevelMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()