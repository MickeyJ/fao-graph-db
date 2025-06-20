"""Run development_assistance_to_agriculture_receives_from migration"""
from .development_assistance_to_agriculture_receives_from import DevelopmentAssistanceToAgricultureReceives_FromMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute development_assistance_to_agriculture_receives_from migration"""
    try:
        migrator = DevelopmentAssistanceToAgricultureReceives_FromMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()