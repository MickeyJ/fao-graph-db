"""Run emissions_totals_emits migration"""
from .emissions_totals_emits import EmissionsTotalsEmitsMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute emissions_totals_emits migration"""
    try:
        migrator = EmissionsTotalsEmitsMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()