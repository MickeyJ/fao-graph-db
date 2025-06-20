"""Run climate_change_emissions_indicators_emits migration"""
from .climate_change_emissions_indicators_emits import ClimateChangeEmissionsIndicatorsEmitsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute climate_change_emissions_indicators_emits migration"""
    try:
        migrator = ClimateChangeEmissionsIndicatorsEmitsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()