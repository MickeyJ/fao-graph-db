"""Run releas migration"""
from .releas import ReleasMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute releas migration"""
    try:
        migrator = ReleasMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()