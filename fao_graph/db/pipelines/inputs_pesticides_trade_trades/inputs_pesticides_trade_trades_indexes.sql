-- Indexes for TRADES relationships from inputs_pesticides_trade

CREATE INDEX IF NOT EXISTS idx_inputs_pesticides_trade_trades_year
ON fao_graph."TRADES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_inputs_pesticides_trade_trades_value
ON fao_graph."TRADES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_inputs_pesticides_trade_trades_year_code
ON fao_graph."TRADES" USING btree ((properties->>'year_code'));
