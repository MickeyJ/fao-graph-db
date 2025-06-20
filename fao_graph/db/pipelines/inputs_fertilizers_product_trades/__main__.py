"""Run inputs_fertilizers_product_trades migration"""
from .inputs_fertilizers_product_trades import InputsFertilizersProductTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute inputs_fertilizers_product_trades migration"""
    try:
        migrator = InputsFertilizersProductTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()