"""Run forestry_trades migration"""
from .forestry_trades import ForestryTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute forestry_trades migration"""
    try:
        migrator = ForestryTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()