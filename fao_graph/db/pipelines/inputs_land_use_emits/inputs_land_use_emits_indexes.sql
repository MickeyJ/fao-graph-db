-- Indexes for EMITS relationships from inputs_land_use

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_inputs_land_use_emits_element_codes
ON fao_graph."EMITS" USING btree ((properties->>'element_codes'));
CREATE INDEX IF NOT EXISTS idx_inputs_land_use_emits_element
ON fao_graph."EMITS" USING btree ((properties->>'element'));
CREATE INDEX IF NOT EXISTS idx_inputs_land_use_emits_element_code
ON fao_graph."EMITS" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_inputs_land_use_emits_elements
ON fao_graph."EMITS" USING btree ((properties->>'elements'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_inputs_land_use_emits_year
ON fao_graph."EMITS" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_inputs_land_use_emits_value
ON fao_graph."EMITS" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_inputs_land_use_emits_compound
ON fao_graph."EMITS" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_inputs_land_use_emits_source
ON fao_graph."EMITS" USING btree ((properties->>'source_dataset'));