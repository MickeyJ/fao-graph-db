"""Run trade_detailed_trade_matrix_shares migration"""
from .trade_detailed_trade_matrix_shares import TradeDetailedTradeMatrixSharesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute trade_detailed_trade_matrix_shares migration"""
    try:
        migrator = TradeDetailedTradeMatrixSharesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()