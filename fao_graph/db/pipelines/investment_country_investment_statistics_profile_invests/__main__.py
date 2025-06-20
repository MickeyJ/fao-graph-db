"""Run investment_country_investment_statistics_profile_invests migration"""
from .investment_country_investment_statistics_profile_invests import InvestmentCountryInvestmentStatisticsProfileInvestsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute investment_country_investment_statistics_profile_invests migration"""
    try:
        migrator = InvestmentCountryInvestmentStatisticsProfileInvestsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()