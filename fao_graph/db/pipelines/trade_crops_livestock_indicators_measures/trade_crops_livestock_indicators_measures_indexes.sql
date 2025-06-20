-- Indexes for MEASURES relationships from trade_crops_livestock_indicators

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_measures_category
ON fao_graph."MEASURES" USING btree ((properties->>'category'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_measures_indicator_code
ON fao_graph."MEASURES" USING btree ((properties->>'indicator_code'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_measures_indicator
ON fao_graph."MEASURES" USING btree ((properties->>'indicator'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_measures_year
ON fao_graph."MEASURES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_measures_compound
ON fao_graph."MEASURES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_measures_source
ON fao_graph."MEASURES" USING btree ((properties->>'source_dataset'));