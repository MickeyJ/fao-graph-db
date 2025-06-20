"""Run environment_bioenergy_consumes migration"""
from .environment_bioenergy_consumes import EnvironmentBioenergyConsumesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute environment_bioenergy_consumes migration"""
    try:
        migrator = EnvironmentBioenergyConsumesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()