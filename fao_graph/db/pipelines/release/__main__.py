"""Run release migration"""
from .release import ReleaseMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute release migration"""
    try:
        migrator = ReleaseMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()