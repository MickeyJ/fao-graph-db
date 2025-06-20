"""Run environment_cropland_nutrient_budget_utilizes migration"""
from .environment_cropland_nutrient_budget_utilizes import EnvironmentCroplandNutrientBudgetUtilizesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute environment_cropland_nutrient_budget_utilizes migration"""
    try:
        migrator = EnvironmentCroplandNutrientBudgetUtilizesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()