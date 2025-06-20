"""Run inputs_fertilizers_nutrient_trades migration"""
from .inputs_fertilizers_nutrient_trades import InputsFertilizersNutrientTradesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute inputs_fertilizers_nutrient_trades migration"""
    try:
        migrator = InputsFertilizersNutrientTradesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()