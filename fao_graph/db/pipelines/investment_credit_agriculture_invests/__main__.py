"""Run investment_credit_agriculture_invests migration"""
from .investment_credit_agriculture_invests import InvestmentCreditAgricultureInvestsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute investment_credit_agriculture_invests migration"""
    try:
        migrator = InvestmentCreditAgricultureInvestsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()