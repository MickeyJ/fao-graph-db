"""Run consumer_price_indices_measures migration"""
from .consumer_price_indices_measures import ConsumerPriceIndicesMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute consumer_price_indices_measures migration"""
    try:
        migrator = ConsumerPriceIndicesMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()