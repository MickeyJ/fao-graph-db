"""Run individual_quantitative_dietary_data_food_and_diet_measures migration"""
from .individual_quantitative_dietary_data_food_and_diet_measures import IndividualQuantitativeDietaryDataFoodAndDietMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute individual_quantitative_dietary_data_food_and_diet_measures migration"""
    try:
        migrator = IndividualQuantitativeDietaryDataFoodAndDietMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()