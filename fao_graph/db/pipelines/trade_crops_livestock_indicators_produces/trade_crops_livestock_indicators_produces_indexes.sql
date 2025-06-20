-- Indexes for PRODUCES relationships from trade_crops_livestock_indicators

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_produces_measure
ON fao_graph."PRODUCES" USING btree ((properties->>'measure'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_produces_indicator_code
ON fao_graph."PRODUCES" USING btree ((properties->>'indicator_code'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_produces_indicator
ON fao_graph."PRODUCES" USING btree ((properties->>'indicator'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_produces_year
ON fao_graph."PRODUCES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_produces_value
ON fao_graph."PRODUCES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_produces_compound
ON fao_graph."PRODUCES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_produces_source
ON fao_graph."PRODUCES" USING btree ((properties->>'source_dataset'));