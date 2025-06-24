"""
Migration pipeline for food_balance_sheets__uses
Generated from YAML configuration
"""
from fao_graph.db.pipelines.food_balance_sheets__uses.food_balance_sheets__uses import FoodBalanceSheetsUsesMigrator


def main():
    """Run the migration"""
    migrator = FoodBalanceSheetsUsesMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()