"""Run fertilizers_detailed_trade_matrix_trades migration"""
from .fertilizers_detailed_trade_matrix_trades import FertilizersDetailedTradeMatrixTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute fertilizers_detailed_trade_matrix_trades migration"""
    try:
        migrator = FertilizersDetailedTradeMatrixTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()