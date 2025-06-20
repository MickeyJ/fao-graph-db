"""Run inputs_pesticides_use_uses migration"""
from .inputs_pesticides_use_uses import InputsPesticidesUseUsesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute inputs_pesticides_use_uses migration"""
    try:
        migrator = InputsPesticidesUseUsesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()