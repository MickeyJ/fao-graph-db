"""Run forestry_measures migration"""
from .forestry_measures import ForestryMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute forestry_measures migration"""
    try:
        migrator = ForestryMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()