"""Run forestry_produces migration"""
from .forestry_produces import ForestryProducesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute forestry_produces migration"""
    try:
        migrator = ForestryProducesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()