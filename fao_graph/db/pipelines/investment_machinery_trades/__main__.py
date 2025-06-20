"""Run investment_machinery_trades migration"""
from .investment_machinery_trades import InvestmentMachineryTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute investment_machinery_trades migration"""
    try:
        migrator = InvestmentMachineryTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()