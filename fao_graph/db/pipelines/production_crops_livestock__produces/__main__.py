"""
Migration pipeline for production_crops_livestock__produces
Generated from YAML configuration
"""
from fao_graph.db.pipelines.production_crops_livestock__produces.production_crops_livestock__produces import ProductionCropsLivestockProducesMigrator


def main():
    """Run the migration"""
    migrator = ProductionCropsLivestockProducesMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()