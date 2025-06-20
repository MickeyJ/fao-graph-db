"""Run flag migration"""
from .flag import FlagMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute flag migration"""
    try:
        migrator = FlagMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()