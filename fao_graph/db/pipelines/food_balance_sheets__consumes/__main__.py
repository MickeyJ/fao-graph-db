"""
Migration pipeline for food_balance_sheets__consumes
Generated from YAML configuration
"""
from fao_graph.db.pipelines.food_balance_sheets__consumes.food_balance_sheets__consumes import FoodBalanceSheetsConsumesMigrator


def main():
    """Run the migration"""
    migrator = FoodBalanceSheetsConsumesMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()