"""Run investment_machinery_measures migration"""
from .investment_machinery_measures import InvestmentMachineryMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute investment_machinery_measures migration"""
    try:
        migrator = InvestmentMachineryMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()