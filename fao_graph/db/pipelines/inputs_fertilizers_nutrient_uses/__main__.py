"""Run inputs_fertilizers_nutrient_uses migration"""
from .inputs_fertilizers_nutrient_uses import InputsFertilizersNutrientUsesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute inputs_fertilizers_nutrient_uses migration"""
    try:
        migrator = InputsFertilizersNutrientUsesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()