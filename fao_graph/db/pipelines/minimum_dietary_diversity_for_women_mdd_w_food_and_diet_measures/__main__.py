"""Run minimum_dietary_diversity_for_women_mdd_w_food_and_diet_measures migration"""
from .minimum_dietary_diversity_for_women_mdd_w_food_and_diet_measures import MinimumDietaryDiversityForWomenMddWFoodAndDietMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute minimum_dietary_diversity_for_women_mdd_w_food_and_diet_measures migration"""
    try:
        migrator = MinimumDietaryDiversityForWomenMddWFoodAndDietMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()