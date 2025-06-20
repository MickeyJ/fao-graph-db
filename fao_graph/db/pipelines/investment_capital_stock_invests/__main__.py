"""Run investment_capital_stock_invests migration"""
from .investment_capital_stock_invests import InvestmentCapitalStockInvestsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute investment_capital_stock_invests migration"""
    try:
        migrator = InvestmentCapitalStockInvestsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()