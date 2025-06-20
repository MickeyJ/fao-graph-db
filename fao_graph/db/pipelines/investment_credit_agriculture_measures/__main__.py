"""Run investment_credit_agriculture_measures migration"""
from .investment_credit_agriculture_measures import InvestmentCreditAgricultureMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute investment_credit_agriculture_measures migration"""
    try:
        migrator = InvestmentCreditAgricultureMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()