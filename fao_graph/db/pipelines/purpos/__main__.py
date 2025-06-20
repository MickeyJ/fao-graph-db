"""Run purpos migration"""
from .purpos import PurposMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute purpos migration"""
    try:
        migrator = PurposMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()