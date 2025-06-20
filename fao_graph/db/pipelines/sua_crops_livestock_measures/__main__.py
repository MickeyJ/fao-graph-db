"""Run sua_crops_livestock_measures migration"""
from .sua_crops_livestock_measures import SuaCropsLivestockMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute sua_crops_livestock_measures migration"""
    try:
        migrator = SuaCropsLivestockMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()