"""Run employment_indicators_agriculture_measures migration"""
from .employment_indicators_agriculture_measures import EmploymentIndicatorsAgricultureMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute employment_indicators_agriculture_measures migration"""
    try:
        migrator = EmploymentIndicatorsAgricultureMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()