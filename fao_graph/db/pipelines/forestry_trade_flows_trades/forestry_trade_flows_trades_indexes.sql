-- Indexes for TRADES relationships from forestry_trade_flows

-- Index on relationship properties

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_trades_year
ON fao_graph."TRADES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_trades_value
ON fao_graph."TRADES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_trades_compound
ON fao_graph."TRADES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_forestry_trade_flows_trades_source
ON fao_graph."TRADES" USING btree ((properties->>'source_dataset'));