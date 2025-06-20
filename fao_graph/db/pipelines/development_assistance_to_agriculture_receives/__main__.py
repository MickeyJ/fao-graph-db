"""Run development_assistance_to_agriculture_receives migration"""
from .development_assistance_to_agriculture_receives import DevelopmentAssistanceToAgricultureReceivesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute development_assistance_to_agriculture_receives migration"""
    try:
        migrator = DevelopmentAssistanceToAgricultureReceivesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()