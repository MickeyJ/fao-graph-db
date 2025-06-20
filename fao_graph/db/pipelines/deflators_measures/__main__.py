"""Run deflators_measures migration"""
from .deflators_measures import DeflatorsMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute deflators_measures migration"""
    try:
        migrator = DeflatorsMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()