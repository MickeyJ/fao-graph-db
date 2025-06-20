"""Run emissions_land_use_forests_emits migration"""
from .emissions_land_use_forests_emits import EmissionsLandUseForestsEmitsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute emissions_land_use_forests_emits migration"""
    try:
        migrator = EmissionsLandUseForestsEmitsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()