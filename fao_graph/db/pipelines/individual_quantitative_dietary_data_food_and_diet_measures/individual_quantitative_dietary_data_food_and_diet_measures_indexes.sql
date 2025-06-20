-- Indexes for MEASURES relationships from individual_quantitative_dietary_data_food_and_diet

-- Index on relationship properties

-- Index on data properties


CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_measures_compound
ON fao_graph."MEASURES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_measures_source
ON fao_graph."MEASURES" USING btree ((properties->>'source_dataset'));