-- Indexes for TRADES relationships from trade_detailed_trade_matrix

CREATE INDEX IF NOT EXISTS idx_trade_detailed_trade_matrix_trades_year
ON fao_graph."TRADES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_trade_detailed_trade_matrix_trades_value
ON fao_graph."TRADES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_trade_detailed_trade_matrix_trades_year_code
ON fao_graph."TRADES" USING btree ((properties->>'year_code'));
