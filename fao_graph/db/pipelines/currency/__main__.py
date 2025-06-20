"""Run currency migration"""
from .currency import CurrencyMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute currency migration"""
    try:
        migrator = CurrencyMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()