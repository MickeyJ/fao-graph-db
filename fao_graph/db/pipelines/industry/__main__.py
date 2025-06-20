"""Run industry migration"""
from .industry import IndustryMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute industry migration"""
    try:
        migrator = IndustryMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()