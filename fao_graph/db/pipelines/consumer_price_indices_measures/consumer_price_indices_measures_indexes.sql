-- Indexes for MEASURES relationships from consumer_price_indices

CREATE INDEX IF NOT EXISTS idx_consumer_price_indices_measures_year
ON fao_graph."MEASURES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_consumer_price_indices_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_consumer_price_indices_measures_year_code
ON fao_graph."MEASURES" USING btree ((properties->>'year_code'));
