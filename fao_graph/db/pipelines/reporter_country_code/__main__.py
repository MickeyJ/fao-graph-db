"""
Migration pipeline for reporter_country_code
Generated from YAML configuration
"""
from fao_graph.db.pipelines.reporter_country_code.reporter_country_code import ReporterCountryCodeMigrator


def main():
    """Run the migration"""
    migrator = ReporterCountryCodeMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()