"""Run emissions_land_use_fires_emits migration"""
from .emissions_land_use_fires_emits import EmissionsLandUseFiresEmitsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute emissions_land_use_fires_emits migration"""
    try:
        migrator = EmissionsLandUseFiresEmitsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()