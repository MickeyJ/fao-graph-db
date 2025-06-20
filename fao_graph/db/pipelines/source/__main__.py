"""Run source migration"""
from .source import SourceMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute source migration"""
    try:
        migrator = SourceMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()