"""Run indicators_from_household_surveys_measures migration"""
from .indicators_from_household_surveys_measures import IndicatorsFromHouseholdSurveysMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute indicators_from_household_surveys_measures migration"""
    try:
        migrator = IndicatorsFromHouseholdSurveysMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()