-- Indexes for MEASURES relationships from prices

CREATE INDEX IF NOT EXISTS idx_prices_measures_year
ON fao_graph."MEASURES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_prices_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_prices_measures_year_code
ON fao_graph."MEASURES" USING btree ((properties->>'year_code'));
