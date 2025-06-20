"""Run reporter_country_code migration"""
from .reporter_country_code import ReporterCountryCodeMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute reporter_country_code migration"""
    try:
        migrator = ReporterCountryCodeMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()