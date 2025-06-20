"""Run element migration"""
from .element import ElementMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute element migration"""
    try:
        migrator = ElementMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()