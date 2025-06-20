"""Run sua_crops_livestock_produces migration"""
from .sua_crops_livestock_produces import SuaCropsLivestockProducesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute sua_crops_livestock_produces migration"""
    try:
        migrator = SuaCropsLivestockProducesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()