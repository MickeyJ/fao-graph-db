"""Run environment_bioenergy_produces migration"""
from .environment_bioenergy_produces import EnvironmentBioenergyProducesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute environment_bioenergy_produces migration"""
    try:
        migrator = EnvironmentBioenergyProducesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()