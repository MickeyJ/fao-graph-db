-- Indexes for TRADES relationships from commodity_balances_non_food_2013_old_methodology

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_commodity_balances_non_food_2013_old_methodology_trades_element_codes
ON fao_graph."TRADES" USING btree ((properties->>'element_codes'));
CREATE INDEX IF NOT EXISTS idx_commodity_balances_non_food_2013_old_methodology_trades_element
ON fao_graph."TRADES" USING btree ((properties->>'element'));
CREATE INDEX IF NOT EXISTS idx_commodity_balances_non_food_2013_old_methodology_trades_element_code
ON fao_graph."TRADES" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_commodity_balances_non_food_2013_old_methodology_trades_elements
ON fao_graph."TRADES" USING btree ((properties->>'elements'));
CREATE INDEX IF NOT EXISTS idx_commodity_balances_non_food_2013_old_methodology_trades_flow_direction
ON fao_graph."TRADES" USING btree ((properties->>'flow_direction'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_commodity_balances_non_food_2013_old_methodology_trades_year
ON fao_graph."TRADES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_commodity_balances_non_food_2013_old_methodology_trades_value
ON fao_graph."TRADES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_commodity_balances_non_food_2013_old_methodology_trades_compound
ON fao_graph."TRADES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_commodity_balances_non_food_2013_old_methodology_trades_source
ON fao_graph."TRADES" USING btree ((properties->>'source_dataset'));