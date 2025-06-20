"""Run employment_indicators_agriculture_employs migration"""
from .employment_indicators_agriculture_employs import EmploymentIndicatorsAgricultureEmploysMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute employment_indicators_agriculture_employs migration"""
    try:
        migrator = EmploymentIndicatorsAgricultureEmploysMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()