"""Run population_measures migration"""
from .population_measures import PopulationMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute population_measures migration"""
    try:
        migrator = PopulationMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()