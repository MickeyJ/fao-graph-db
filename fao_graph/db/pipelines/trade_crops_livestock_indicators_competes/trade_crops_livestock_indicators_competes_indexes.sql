-- Indexes for COMPETES relationships from trade_crops_livestock_indicators

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_competes_measure
ON fao_graph."COMPETES" USING btree ((properties->>'measure'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_competes_indicator_code
ON fao_graph."COMPETES" USING btree ((properties->>'indicator_code'));
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_competes_indicator
ON fao_graph."COMPETES" USING btree ((properties->>'indicator'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_competes_year
ON fao_graph."COMPETES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_competes_value
ON fao_graph."COMPETES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_competes_compound
ON fao_graph."COMPETES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_trade_crops_livestock_indicators_competes_source
ON fao_graph."COMPETES" USING btree ((properties->>'source_dataset'));