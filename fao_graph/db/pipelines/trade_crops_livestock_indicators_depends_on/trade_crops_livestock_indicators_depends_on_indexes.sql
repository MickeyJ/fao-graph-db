-- Indexes for DEPENDS_ON relationships from trade_crops_livestock_indicators

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_depends_on_measure
ON fao_graph."DEPENDS_ON" USING btree ((properties->>'measure'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_depends_on_indicator_code
ON fao_graph."DEPENDS_ON" USING btree ((properties->>'indicator_code'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_depends_on_indicator
ON fao_graph."DEPENDS_ON" USING btree ((properties->>'indicator'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_depends_on_year
ON fao_graph."DEPENDS_ON" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_depends_on_value
ON fao_graph."DEPENDS_ON" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_depends_on_compound
ON fao_graph."DEPENDS_ON" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_depends_on_source
ON fao_graph."DEPENDS_ON" USING btree ((properties->>'source_dataset'));