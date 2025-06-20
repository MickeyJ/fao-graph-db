"""Run asti_expenditures_employs migration"""
from .asti_expenditures_employs import AstiExpendituresEmploysMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute asti_expenditures_employs migration"""
    try:
        migrator = AstiExpendituresEmploysMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()