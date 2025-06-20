"""Run trade_indices_trades migration"""
from .trade_indices_trades import TradeIndicesTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute trade_indices_trades migration"""
    try:
        migrator = TradeIndicesTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()