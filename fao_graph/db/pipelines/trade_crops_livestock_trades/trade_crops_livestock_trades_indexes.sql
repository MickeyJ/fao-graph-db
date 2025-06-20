-- Indexes for TRADES relationships from trade_crops_livestock

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_trades_flow
ON fao_graph."TRADES" USING btree ((properties->>'flow'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_trades_content_type
ON fao_graph."TRADES" USING btree ((properties->>'content_type'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_trades_nutrient
ON fao_graph."TRADES" USING btree ((properties->>'nutrient'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_trades_measure
ON fao_graph."TRADES" USING btree ((properties->>'measure'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_trades_element_code
ON fao_graph."TRADES" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_trades_element
ON fao_graph."TRADES" USING btree ((properties->>'element'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_trades_year
ON fao_graph."TRADES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_trades_value
ON fao_graph."TRADES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_trades_compound
ON fao_graph."TRADES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_trades_source
ON fao_graph."TRADES" USING btree ((properties->>'source_dataset'));