"""
Migration pipeline for food_security_data__experiences
Generated from YAML configuration
"""
from fao_graph.db.pipelines.food_security_data__experiences.food_security_data__experiences import FoodSecurityDataExperiencesMigrator


def main():
    """Run the migration"""
    migrator = FoodSecurityDataExperiencesMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()