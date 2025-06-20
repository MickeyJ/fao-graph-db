"""Run forestry_trade_flows_shares migration"""
from .forestry_trade_flows_shares import ForestryTradeFlowsSharesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute forestry_trade_flows_shares migration"""
    try:
        migrator = ForestryTradeFlowsSharesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()