"""
Migration pipeline for trade_detailed_trade_matrix__imports
Generated from YAML configuration
"""
from fao_graph.db.pipelines.trade_detailed_trade_matrix__imports.trade_detailed_trade_matrix__imports import TradeDetailedTradeMatrixImportsMigrator


def main():
    """Run the migration"""
    migrator = TradeDetailedTradeMatrixImportsMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()