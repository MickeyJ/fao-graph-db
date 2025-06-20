"""Run item_code migration"""
from .item_code import ItemCodeMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute item_code migration"""
    try:
        migrator = ItemCodeMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()