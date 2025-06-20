"""Run environment_land_cover_measures migration"""
from .environment_land_cover_measures import EnvironmentLandCoverMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute environment_land_cover_measures migration"""
    try:
        migrator = EnvironmentLandCoverMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()