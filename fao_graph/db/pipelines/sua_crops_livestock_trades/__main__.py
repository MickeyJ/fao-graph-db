"""Run sua_crops_livestock_trades migration"""
from .sua_crops_livestock_trades import SuaCropsLivestockTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute sua_crops_livestock_trades migration"""
    try:
        migrator = SuaCropsLivestockTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()