-- Indexes for MEASURES relationships from employment_indicators_agriculture

-- Index on relationship properties

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