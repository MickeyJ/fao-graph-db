"""Run emissions_agriculture_energy_emits migration"""
from .emissions_agriculture_energy_emits import EmissionsAgricultureEnergyEmitsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute emissions_agriculture_energy_emits migration"""
    try:
        migrator = EmissionsAgricultureEnergyEmitsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()