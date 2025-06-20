"""Run sua_crops_livestock_supplies migration"""
from .sua_crops_livestock_supplies import SuaCropsLivestockSuppliesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute sua_crops_livestock_supplies migration"""
    try:
        migrator = SuaCropsLivestockSuppliesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()