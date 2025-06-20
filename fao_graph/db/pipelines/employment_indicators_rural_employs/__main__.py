"""Run employment_indicators_rural_employs migration"""
from .employment_indicators_rural_employs import EmploymentIndicatorsRuralEmploysMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute employment_indicators_rural_employs migration"""
    try:
        migrator = EmploymentIndicatorsRuralEmploysMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()