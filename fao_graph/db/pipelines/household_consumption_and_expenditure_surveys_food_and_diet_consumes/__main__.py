"""Run household_consumption_and_expenditure_surveys_food_and_diet_consumes migration"""
from .household_consumption_and_expenditure_surveys_food_and_diet_consumes import HouseholdConsumptionAndExpenditureSurveysFoodAndDietConsumesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute household_consumption_and_expenditure_surveys_food_and_diet_consumes migration"""
    try:
        migrator = HouseholdConsumptionAndExpenditureSurveysFoodAndDietConsumesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()