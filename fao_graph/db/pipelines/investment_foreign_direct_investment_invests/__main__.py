"""Run investment_foreign_direct_investment_invests migration"""
from .investment_foreign_direct_investment_invests import InvestmentForeignDirectInvestmentInvestsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute investment_foreign_direct_investment_invests migration"""
    try:
        migrator = InvestmentForeignDirectInvestmentInvestsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()