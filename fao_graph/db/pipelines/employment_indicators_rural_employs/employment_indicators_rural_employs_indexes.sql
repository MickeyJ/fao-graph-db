-- Indexes for EMPLOYS relationships from employment_indicators_rural

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_employment_indicators_rural_employs_indicator_codes
ON fao_graph."EMPLOYS" USING btree ((properties->>'indicator_codes'));
CREATE INDEX IF NOT EXISTS idx_employment_indicators_rural_employs_indicator
ON fao_graph."EMPLOYS" USING btree ((properties->>'indicator'));
CREATE INDEX IF NOT EXISTS idx_employment_indicators_rural_employs_indicator_code
ON fao_graph."EMPLOYS" USING btree ((properties->>'indicator_code'));
CREATE INDEX IF NOT EXISTS idx_employment_indicators_rural_employs_indicators
ON fao_graph."EMPLOYS" USING btree ((properties->>'indicators'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_employment_indicators_rural_employs_year
ON fao_graph."EMPLOYS" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_employment_indicators_rural_employs_value
ON fao_graph."EMPLOYS" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_employment_indicators_rural_employs_compound
ON fao_graph."EMPLOYS" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_employment_indicators_rural_employs_source
ON fao_graph."EMPLOYS" USING btree ((properties->>'source_dataset'));