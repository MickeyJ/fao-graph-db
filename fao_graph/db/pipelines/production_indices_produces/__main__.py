"""Run production_indices_produces migration"""
from .production_indices_produces import ProductionIndicesProducesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute production_indices_produces migration"""
    try:
        migrator = ProductionIndicesProducesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()