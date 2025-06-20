"""Run prices_produces migration"""
from .prices_produces import PricesProducesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute prices_produces migration"""
    try:
        migrator = PricesProducesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()