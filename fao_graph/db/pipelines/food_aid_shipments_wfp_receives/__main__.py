"""Run food_aid_shipments_wfp_receives migration"""
from .food_aid_shipments_wfp_receives import FoodAidShipmentsWfpReceivesMigrator
from fao_graph.logger import logger


def run_migration():
    """Execute food_aid_shipments_wfp_receives migration"""
    try:
        migrator = FoodAidShipmentsWfpReceivesMigrator()
        migrator.migrate()
        migrator.verify_migration()
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        raise


if __name__ == "__main__":
    run_migration()