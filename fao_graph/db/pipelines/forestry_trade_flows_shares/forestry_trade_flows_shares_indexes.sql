-- Indexes for SHARES relationships from forestry_trade_flows

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_shares_pattern
ON fao_graph."SHARES" USING btree ((properties->>'pattern'));
CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_shares_source_fk
ON fao_graph."SHARES" USING btree ((properties->>'source_fk'));
CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_shares_target_fk
ON fao_graph."SHARES" USING btree ((properties->>'target_fk'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_shares_year
ON fao_graph."SHARES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_shares_value
ON fao_graph."SHARES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_shares_compound
ON fao_graph."SHARES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_shares_source
ON fao_graph."SHARES" USING btree ((properties->>'source_dataset'));