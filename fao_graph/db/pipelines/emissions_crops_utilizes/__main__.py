"""Run emissions_crops_utilizes migration"""
from .emissions_crops_utilizes import EmissionsCropsUtilizesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute emissions_crops_utilizes migration"""
    try:
        migrator = EmissionsCropsUtilizesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()