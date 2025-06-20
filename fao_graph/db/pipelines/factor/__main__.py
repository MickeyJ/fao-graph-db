"""Run factor migration"""
from .factor import FactorMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute factor migration"""
    try:
        migrator = FactorMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()