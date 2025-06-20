"""Run exchange_rate_exchanges migration"""
from .exchange_rate_exchanges import ExchangeRateExchangesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute exchange_rate_exchanges migration"""
    try:
        migrator = ExchangeRateExchangesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()