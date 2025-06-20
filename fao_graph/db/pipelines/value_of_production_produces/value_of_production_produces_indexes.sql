-- Indexes for PRODUCES relationships from value_of_production

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_value_of_production_produces_element_codes
ON fao_graph."PRODUCES" USING btree ((properties->>'element_codes'));
CREATE INDEX IF NOT EXISTS idx_value_of_production_produces_element
ON fao_graph."PRODUCES" USING btree ((properties->>'element'));
CREATE INDEX IF NOT EXISTS idx_value_of_production_produces_element_code
ON fao_graph."PRODUCES" USING btree ((properties->>'element_code'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_value_of_production_produces_year
ON fao_graph."PRODUCES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_value_of_production_produces_value
ON fao_graph."PRODUCES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_value_of_production_produces_compound
ON fao_graph."PRODUCES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_value_of_production_produces_source
ON fao_graph."PRODUCES" USING btree ((properties->>'source_dataset'));