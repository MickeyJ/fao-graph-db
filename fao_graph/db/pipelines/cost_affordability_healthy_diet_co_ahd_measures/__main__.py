"""Run cost_affordability_healthy_diet_co_ahd_measures migration"""
from .cost_affordability_healthy_diet_co_ahd_measures import CostAffordabilityHealthyDietCoAhdMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute cost_affordability_healthy_diet_co_ahd_measures migration"""
    try:
        migrator = CostAffordabilityHealthyDietCoAhdMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()