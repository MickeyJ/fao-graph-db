-- Indexes for indicator nodes
CREATE INDEX IF NOT EXISTS idx_indicators_indicator_code
ON fao.indicator USING btree ((properties->>'indicator_code'));

CREATE INDEX IF NOT EXISTS idx_indicators_source_dataset  
ON fao.indicator USING btree ((properties->>'source_dataset'));

