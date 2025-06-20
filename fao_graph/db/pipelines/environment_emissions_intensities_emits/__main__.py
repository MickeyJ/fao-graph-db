"""Run environment_emissions_intensities_emits migration"""
from .environment_emissions_intensities_emits import EnvironmentEmissionsIntensitiesEmitsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute environment_emissions_intensities_emits migration"""
    try:
        migrator = EnvironmentEmissionsIntensitiesEmitsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()