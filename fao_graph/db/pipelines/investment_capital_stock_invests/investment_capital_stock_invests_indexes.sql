-- Indexes for INVESTS relationships from investment_capital_stock

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_investment_capital_stock_invests_element_codes
ON fao_graph."INVESTS" USING btree ((properties->>'element_codes'));
CREATE INDEX IF NOT EXISTS idx_investment_capital_stock_invests_element
ON fao_graph."INVESTS" USING btree ((properties->>'element'));
CREATE INDEX IF NOT EXISTS idx_investment_capital_stock_invests_element_code
ON fao_graph."INVESTS" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_investment_capital_stock_invests_elements
ON fao_graph."INVESTS" USING btree ((properties->>'elements'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_investment_capital_stock_invests_year
ON fao_graph."INVESTS" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_investment_capital_stock_invests_value
ON fao_graph."INVESTS" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_investment_capital_stock_invests_compound
ON fao_graph."INVESTS" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_investment_capital_stock_invests_source
ON fao_graph."INVESTS" USING btree ((properties->>'source_dataset'));