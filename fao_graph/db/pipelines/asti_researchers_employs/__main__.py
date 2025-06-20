"""Run asti_researchers_employs migration"""
from .asti_researchers_employs import AstiResearchersEmploysMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute asti_researchers_employs migration"""
    try:
        migrator = AstiResearchersEmploysMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()