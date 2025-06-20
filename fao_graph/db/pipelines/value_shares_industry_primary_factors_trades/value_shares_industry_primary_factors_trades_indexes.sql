-- Indexes for TRADES relationships from value_shares_industry_primary_factors

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_value_shares_industry_primary_factors_trades_industry_codes
ON fao_graph."TRADES" USING btree ((properties->>'industry_codes'));
CREATE INDEX IF NOT EXISTS idx_value_shares_industry_primary_factors_trades_industry
ON fao_graph."TRADES" USING btree ((properties->>'industry'));
CREATE INDEX IF NOT EXISTS idx_value_shares_industry_primary_factors_trades_industry_code
ON fao_graph."TRADES" USING btree ((properties->>'industry_code'));
CREATE INDEX IF NOT EXISTS idx_value_shares_industry_primary_factors_trades_flow_direction
ON fao_graph."TRADES" USING btree ((properties->>'flow_direction'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_value_shares_industry_primary_factors_trades_year
ON fao_graph."TRADES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_value_shares_industry_primary_factors_trades_value
ON fao_graph."TRADES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_value_shares_industry_primary_factors_trades_compound
ON fao_graph."TRADES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_value_shares_industry_primary_factors_trades_source
ON fao_graph."TRADES" USING btree ((properties->>'source_dataset'));