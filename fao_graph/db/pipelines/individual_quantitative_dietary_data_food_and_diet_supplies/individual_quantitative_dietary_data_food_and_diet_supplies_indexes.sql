-- Indexes for SUPPLIES relationships from individual_quantitative_dietary_data_food_and_diet

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_supplies_element_codes
ON fao_graph."SUPPLIES" USING btree ((properties->>'element_codes'));
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_supplies_element
ON fao_graph."SUPPLIES" USING btree ((properties->>'element'));
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_supplies_element_code
ON fao_graph."SUPPLIES" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_supplies_elements
ON fao_graph."SUPPLIES" USING btree ((properties->>'elements'));

-- Index on data properties


CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_supplies_value
ON fao_graph."SUPPLIES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_supplies_compound
ON fao_graph."SUPPLIES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_supplies_source
ON fao_graph."SUPPLIES" USING btree ((properties->>'source_dataset'));