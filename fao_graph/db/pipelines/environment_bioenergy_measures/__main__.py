"""Run environment_bioenergy_measures migration"""
from .environment_bioenergy_measures import EnvironmentBioenergyMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute environment_bioenergy_measures migration"""
    try:
        migrator = EnvironmentBioenergyMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()