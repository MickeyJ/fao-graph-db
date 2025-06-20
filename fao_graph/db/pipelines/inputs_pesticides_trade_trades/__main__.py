"""Run inputs_pesticides_trade_trades migration"""
from .inputs_pesticides_trade_trades import InputsPesticidesTradeTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute inputs_pesticides_trade_trades migration"""
    try:
        migrator = InputsPesticidesTradeTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()