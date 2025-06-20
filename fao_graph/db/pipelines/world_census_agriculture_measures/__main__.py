"""Run world_census_agriculture_measures migration"""
from .world_census_agriculture_measures import WorldCensusAgricultureMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute world_census_agriculture_measures migration"""
    try:
        migrator = WorldCensusAgricultureMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()