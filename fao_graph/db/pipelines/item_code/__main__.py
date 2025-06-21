"""
Migration pipeline for item_code
Generated from YAML configuration
"""
from fao_graph.db.pipelines.item_code.item_code import ItemCodeMigrator


def main():
    """Run the migration"""
    migrator = ItemCodeMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()