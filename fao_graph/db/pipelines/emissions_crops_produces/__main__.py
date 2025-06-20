"""Run emissions_crops_produces migration"""
from .emissions_crops_produces import EmissionsCropsProducesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute emissions_crops_produces migration"""
    try:
        migrator = EmissionsCropsProducesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()