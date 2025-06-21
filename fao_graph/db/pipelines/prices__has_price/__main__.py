"""
Migration pipeline for prices__has_price
Generated from YAML configuration
"""
from fao_graph.db.pipelines.prices__has_price.prices__has_price import PricesHasPriceMigrator


def main():
    """Run the migration"""
    migrator = PricesHasPriceMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()