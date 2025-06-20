"""Run indicator migration"""
from .indicator import IndicatorMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute indicator migration"""
    try:
        migrator = IndicatorMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()