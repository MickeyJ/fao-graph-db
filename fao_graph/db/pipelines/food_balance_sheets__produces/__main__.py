"""
Migration pipeline for food_balance_sheets__produces
Generated from YAML configuration
"""
from fao_graph.db.pipelines.food_balance_sheets__produces.food_balance_sheets__produces import FoodBalanceSheetsProducesMigrator


def main():
    """Run the migration"""
    migrator = FoodBalanceSheetsProducesMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()