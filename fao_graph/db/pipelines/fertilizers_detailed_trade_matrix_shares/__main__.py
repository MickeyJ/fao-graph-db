"""Run fertilizers_detailed_trade_matrix_shares migration"""
from .fertilizers_detailed_trade_matrix_shares import FertilizersDetailedTradeMatrixSharesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute fertilizers_detailed_trade_matrix_shares migration"""
    try:
        migrator = FertilizersDetailedTradeMatrixSharesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()