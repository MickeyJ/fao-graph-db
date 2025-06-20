-- Indexes for MEASURES relationships from indicators_from_household_surveys

-- Index on relationship properties

-- Index on data properties


CREATE INDEX IF NOT EXISTS idx_indicators_from_household_surveys_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_indicators_from_household_surveys_measures_compound
ON fao_graph."MEASURES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_indicators_from_household_surveys_measures_source
ON fao_graph."MEASURES" USING btree ((properties->>'source_dataset'));