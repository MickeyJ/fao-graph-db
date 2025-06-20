"""Run inputs_fertilizers_product_uses migration"""
from .inputs_fertilizers_product_uses import InputsFertilizersProductUsesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute inputs_fertilizers_product_uses migration"""
    try:
        migrator = InputsFertilizersProductUsesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()