"""Run emissions_livestock_emits migration"""
from .emissions_livestock_emits import EmissionsLivestockEmitsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute emissions_livestock_emits migration"""
    try:
        migrator = EmissionsLivestockEmitsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()