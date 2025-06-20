"""Run purpose migration"""
from .purpose import PurposeMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute purpose migration"""
    try:
        migrator = PurposeMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()