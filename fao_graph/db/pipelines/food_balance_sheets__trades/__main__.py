"""
Migration pipeline for food_balance_sheets__trades
Generated from YAML configuration
"""
from fao_graph.db.pipelines.food_balance_sheets__trades.food_balance_sheets__trades import FoodBalanceSheetsTradesMigrator


def main():
    """Run the migration"""
    migrator = FoodBalanceSheetsTradesMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()