"""Run food_value migration"""
from .food_value import FoodValueMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute food_value migration"""
    try:
        migrator = FoodValueMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()