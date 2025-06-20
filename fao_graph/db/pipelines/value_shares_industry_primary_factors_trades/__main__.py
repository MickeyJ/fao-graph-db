"""Run value_shares_industry_primary_factors_trades migration"""
from .value_shares_industry_primary_factors_trades import ValueSharesIndustryPrimaryFactorsTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute value_shares_industry_primary_factors_trades migration"""
    try:
        migrator = ValueSharesIndustryPrimaryFactorsTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()