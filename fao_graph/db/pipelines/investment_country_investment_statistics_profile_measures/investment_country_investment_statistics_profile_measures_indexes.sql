-- Indexes for MEASURES relationships from investment_country_investment_statistics_profile

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_investment_country_investment_statistics_profile_measures_element_codes
ON fao_graph."MEASURES" USING btree ((properties->>'element_codes'));
CREATE INDEX IF NOT EXISTS idx_investment_country_investment_statistics_profile_measures_element
ON fao_graph."MEASURES" USING btree ((properties->>'element'));
CREATE INDEX IF NOT EXISTS idx_investment_country_investment_statistics_profile_measures_element_code
ON fao_graph."MEASURES" USING btree ((properties->>'element_code'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_investment_country_investment_statistics_profile_measures_year
ON fao_graph."MEASURES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_investment_country_investment_statistics_profile_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_investment_country_investment_statistics_profile_measures_compound
ON fao_graph."MEASURES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_investment_country_investment_statistics_profile_measures_source
ON fao_graph."MEASURES" USING btree ((properties->>'source_dataset'));