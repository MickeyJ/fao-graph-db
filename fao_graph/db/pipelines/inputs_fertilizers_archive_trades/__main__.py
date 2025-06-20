"""Run inputs_fertilizers_archive_trades migration"""
from .inputs_fertilizers_archive_trades import InputsFertilizersArchiveTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute inputs_fertilizers_archive_trades migration"""
    try:
        migrator = InputsFertilizersArchiveTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()