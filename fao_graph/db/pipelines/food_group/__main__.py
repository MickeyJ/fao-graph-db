"""Run food_group migration"""
from .food_group import FoodGroupMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute food_group migration"""
    try:
        migrator = FoodGroupMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()