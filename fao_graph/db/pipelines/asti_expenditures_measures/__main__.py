"""Run asti_expenditures_measures migration"""
from .asti_expenditures_measures import AstiExpendituresMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute asti_expenditures_measures migration"""
    try:
        migrator = AstiExpendituresMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()