"""Run emissions_pre_post_production_utilizes migration"""
from .emissions_pre_post_production_utilizes import EmissionsPrePostProductionUtilizesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute emissions_pre_post_production_utilizes migration"""
    try:
        migrator = EmissionsPrePostProductionUtilizesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()