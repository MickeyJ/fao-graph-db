"""Run population_age_group migration"""
from .population_age_group import PopulationAgeGroupMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute population_age_group migration"""
    try:
        migrator = PopulationAgeGroupMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()