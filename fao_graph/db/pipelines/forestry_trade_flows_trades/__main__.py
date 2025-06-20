"""Run forestry_trade_flows_trades migration"""
from .forestry_trade_flows_trades import ForestryTradeFlowsTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute forestry_trade_flows_trades migration"""
    try:
        migrator = ForestryTradeFlowsTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()