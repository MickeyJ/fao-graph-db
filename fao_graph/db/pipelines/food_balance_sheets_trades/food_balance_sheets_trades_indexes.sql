-- Indexes for TRADES relationships from food_balance_sheets

CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_trades_year
ON fao_graph."TRADES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_trades_value
ON fao_graph."TRADES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_trades_year_code
ON fao_graph."TRADES" USING btree ((properties->>'year_code'));
