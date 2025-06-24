"""
Migration pipeline for trade_detailed_trade_matrix__exports
Generated from YAML configuration
"""
from fao_graph.db.pipelines.trade_detailed_trade_matrix__exports.trade_detailed_trade_matrix__exports import TradeDetailedTradeMatrixExportsMigrator


def main():
    """Run the migration"""
    migrator = TradeDetailedTradeMatrixExportsMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()