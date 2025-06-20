"""Run sua_crops_livestock_uses migration"""
from .sua_crops_livestock_uses import SuaCropsLivestockUsesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute sua_crops_livestock_uses migration"""
    try:
        migrator = SuaCropsLivestockUsesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()