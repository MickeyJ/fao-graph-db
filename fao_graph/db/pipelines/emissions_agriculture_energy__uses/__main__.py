"""
Migration pipeline for emissions_agriculture_energy__uses
Generated from YAML configuration
"""
from fao_graph.db.pipelines.emissions_agriculture_energy__uses.emissions_agriculture_energy__uses import EmissionsAgricultureEnergyUsesMigrator


def main():
    """Run the migration"""
    migrator = EmissionsAgricultureEnergyUsesMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()