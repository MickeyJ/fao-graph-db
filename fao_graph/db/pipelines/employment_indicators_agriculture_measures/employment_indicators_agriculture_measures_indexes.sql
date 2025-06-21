-- Indexes for MEASURES relationships from employment_indicators_agriculture

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_employment_indicators_agriculture_measures_indicator_codes
ON fao_graph."MEASURES" USING btree ((properties->>'indicator_codes'));
CREATE INDEX IF NOT EXISTS idx_employment_indicators_agriculture_measures_indicator
ON fao_graph."MEASURES" USING btree ((properties->>'indicator'));
CREATE INDEX IF NOT EXISTS idx_employment_indicators_agriculture_measures_indicator_code
ON fao_graph."MEASURES" USING btree ((properties->>'indicator_code'));
CREATE INDEX IF NOT EXISTS idx_employment_indicators_agriculture_measures_indicators
ON fao_graph."MEASURES" USING btree ((properties->>'indicators'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_employment_indicators_agriculture_measures_year
ON fao_graph."MEASURES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_employment_indicators_agriculture_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_employment_indicators_agriculture_measures_compound
ON fao_graph."MEASURES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_employment_indicators_agriculture_measures_source
ON fao_graph."MEASURES" USING btree ((properties->>'source_dataset'));