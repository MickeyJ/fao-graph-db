"""
Migration pipeline for trade_detailed_trade_matrix__trades
Generated from YAML configuration
"""
from fao_graph.db.pipelines.trade_detailed_trade_matrix__trades.trade_detailed_trade_matrix__trades import TradeDetailedTradeMatrixTradesMigrator


def main():
    """Run the migration"""
    migrator = TradeDetailedTradeMatrixTradesMigrator()
    migrator.migrate()


if __name__ == "__main__":
    main()