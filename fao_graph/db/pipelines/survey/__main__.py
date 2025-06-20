"""Run survey migration"""
from .survey import SurveyMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute survey migration"""
    try:
        migrator = SurveyMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()