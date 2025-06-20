"""Run environment_livestock_manure_impacts migration"""
from .environment_livestock_manure_impacts import EnvironmentLivestockManureImpactsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute environment_livestock_manure_impacts migration"""
    try:
        migrator = EnvironmentLivestockManureImpactsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()