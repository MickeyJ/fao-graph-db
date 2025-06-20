-- Indexes for MEASURES relationships from food_security_data

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_food_security_data_measures_element_codes
ON fao_graph."MEASURES" USING btree ((properties->>'element_codes'));
CREATE INDEX IF NOT EXISTS idx_food_security_data_measures_element
ON fao_graph."MEASURES" USING btree ((properties->>'element'));
CREATE INDEX IF NOT EXISTS idx_food_security_data_measures_element_code
ON fao_graph."MEASURES" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_food_security_data_measures_elements
ON fao_graph."MEASURES" USING btree ((properties->>'elements'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_food_security_data_measures_year
ON fao_graph."MEASURES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_food_security_data_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_food_security_data_measures_compound
ON fao_graph."MEASURES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_food_security_data_measures_source
ON fao_graph."MEASURES" USING btree ((properties->>'source_dataset'));