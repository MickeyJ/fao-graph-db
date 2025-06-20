"""Run inputs_fertilizers_nutrient_utilizes migration"""
from .inputs_fertilizers_nutrient_utilizes import InputsFertilizersNutrientUtilizesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute inputs_fertilizers_nutrient_utilizes migration"""
    try:
        migrator = InputsFertilizersNutrientUtilizesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()