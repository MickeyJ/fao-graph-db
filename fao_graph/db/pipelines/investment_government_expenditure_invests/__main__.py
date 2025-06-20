"""Run investment_government_expenditure_invests migration"""
from .investment_government_expenditure_invests import InvestmentGovernmentExpenditureInvestsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute investment_government_expenditure_invests migration"""
    try:
        migrator = InvestmentGovernmentExpenditureInvestsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()