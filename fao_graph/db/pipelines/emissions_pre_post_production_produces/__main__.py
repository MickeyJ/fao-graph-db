"""Run emissions_pre_post_production_produces migration"""
from .emissions_pre_post_production_produces import EmissionsPrePostProductionProducesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute emissions_pre_post_production_produces migration"""
    try:
        migrator = EmissionsPrePostProductionProducesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()