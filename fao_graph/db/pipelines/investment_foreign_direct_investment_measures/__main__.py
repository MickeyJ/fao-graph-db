"""Run investment_foreign_direct_investment_measures migration"""
from .investment_foreign_direct_investment_measures import InvestmentForeignDirectInvestmentMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute investment_foreign_direct_investment_measures migration"""
    try:
        migrator = InvestmentForeignDirectInvestmentMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()