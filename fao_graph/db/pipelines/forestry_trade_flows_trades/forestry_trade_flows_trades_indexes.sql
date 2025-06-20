-- Indexes for TRADES relationships from forestry_trade_flows

CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_trades_year
ON fao_graph."TRADES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_trades_value
ON fao_graph."TRADES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_trades_year_code
ON fao_graph."TRADES" USING btree ((properties->>'year_code'));
