"""
Migration pipeline for emissions_agriculture_energy__emits
Generated from YAML configuration
"""
from fao_graph.db.pipelines.emissions_agriculture_energy__emits.emissions_agriculture_energy__emits import EmissionsAgricultureEnergyEmitsMigrator


def main():
    """Run the migration"""
    migrator = EmissionsAgricultureEnergyEmitsMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()