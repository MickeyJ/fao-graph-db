"""Run environment_livestock_patterns_measures migration"""
from .environment_livestock_patterns_measures import EnvironmentLivestockPatternsMeasuresMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute environment_livestock_patterns_measures migration"""
    try:
        migrator = EnvironmentLivestockPatternsMeasuresMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()