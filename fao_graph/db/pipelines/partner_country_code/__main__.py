"""
Migration pipeline for partner_country_code
Generated from YAML configuration
"""
from fao_graph.db.pipelines.partner_country_code.partner_country_code import PartnerCountryCodeMigrator


def main():
    """Run the migration"""
    migrator = PartnerCountryCodeMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()