"""Run emissions_agriculture_energy_utilizes migration"""
from .emissions_agriculture_energy_utilizes import EmissionsAgricultureEnergyUtilizesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute emissions_agriculture_energy_utilizes migration"""
    try:
        migrator = EmissionsAgricultureEnergyUtilizesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()