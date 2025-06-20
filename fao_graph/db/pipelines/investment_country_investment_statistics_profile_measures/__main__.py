"""Run investment_country_investment_statistics_profile_measures migration"""
from .investment_country_investment_statistics_profile_measures import InvestmentCountryInvestmentStatisticsProfileMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute investment_country_investment_statistics_profile_measures migration"""
    try:
        migrator = InvestmentCountryInvestmentStatisticsProfileMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()