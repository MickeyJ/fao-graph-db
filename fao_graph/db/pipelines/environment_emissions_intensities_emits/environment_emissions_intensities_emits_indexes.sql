-- Indexes for EMITS relationships from environment_emissions_intensities

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_environment_emissions_intensities_emits_source
ON fao_graph."EMITS" USING btree ((properties->>'source'));
CREATE INDEX IF NOT EXISTS idx_environment_emissions_intensities_emits_gas_type
ON fao_graph."EMITS" USING btree ((properties->>'gas_type'));
CREATE INDEX IF NOT EXISTS idx_environment_emissions_intensities_emits_category
ON fao_graph."EMITS" USING btree ((properties->>'category'));
CREATE INDEX IF NOT EXISTS idx_environment_emissions_intensities_emits_element_code
ON fao_graph."EMITS" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_environment_emissions_intensities_emits_element
ON fao_graph."EMITS" USING btree ((properties->>'element'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_environment_emissions_intensities_emits_year
ON fao_graph."EMITS" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_environment_emissions_intensities_emits_value
ON fao_graph."EMITS" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_environment_emissions_intensities_emits_compound
ON fao_graph."EMITS" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_environment_emissions_intensities_emits_source
ON fao_graph."EMITS" USING btree ((properties->>'source_dataset'));