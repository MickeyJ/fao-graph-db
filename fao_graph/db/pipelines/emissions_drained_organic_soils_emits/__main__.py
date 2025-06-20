"""Run emissions_drained_organic_soils_emits migration"""
from .emissions_drained_organic_soils_emits import EmissionsDrainedOrganicSoilsEmitsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute emissions_drained_organic_soils_emits migration"""
    try:
        migrator = EmissionsDrainedOrganicSoilsEmitsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()