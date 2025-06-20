"""Run recipient_country_code migration"""
from .recipient_country_code import RecipientCountryCodeMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute recipient_country_code migration"""
    try:
        migrator = RecipientCountryCodeMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()