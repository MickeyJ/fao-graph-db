"""Run production_crops_livestock_produces migration"""
from .production_crops_livestock_produces import ProductionCropsLivestockProducesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute production_crops_livestock_produces migration"""
    try:
        migrator = ProductionCropsLivestockProducesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()