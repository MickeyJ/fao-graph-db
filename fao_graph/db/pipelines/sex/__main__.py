"""Run sex migration"""
from .sex import SexMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute sex migration"""
    try:
        migrator = SexMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()