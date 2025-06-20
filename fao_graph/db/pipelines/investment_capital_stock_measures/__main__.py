"""Run investment_capital_stock_measures migration"""
from .investment_capital_stock_measures import InvestmentCapitalStockMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute investment_capital_stock_measures migration"""
    try:
        migrator = InvestmentCapitalStockMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()