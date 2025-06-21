"""
Migration pipeline for area_code
Generated from YAML configuration
"""
from fao_graph.db.pipelines.area_code.area_code import AreaCodeMigrator


def main():
    """Run the migration"""
    migrator = AreaCodeMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()