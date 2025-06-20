"""Run inputs_land_use_emits migration"""
from .inputs_land_use_emits import InputsLandUseEmitsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute inputs_land_use_emits migration"""
    try:
        migrator = InputsLandUseEmitsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()