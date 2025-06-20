"""Run partner_country_code migration"""
from .partner_country_code import PartnerCountryCodeMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute partner_country_code migration"""
    try:
        migrator = PartnerCountryCodeMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()