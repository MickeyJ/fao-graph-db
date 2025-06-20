"""Run value_of_production_produces migration"""
from .value_of_production_produces import ValueOfProductionProducesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute value_of_production_produces migration"""
    try:
        migrator = ValueOfProductionProducesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()