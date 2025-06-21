"""
Migration pipeline for food_security_data__measures
Generated from YAML configuration
"""
from fao_graph.db.pipelines.food_security_data__measures.food_security_data__measures import FoodSecurityDataMeasuresMigrator


def main():
    """Run the migration"""
    migrator = FoodSecurityDataMeasuresMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()