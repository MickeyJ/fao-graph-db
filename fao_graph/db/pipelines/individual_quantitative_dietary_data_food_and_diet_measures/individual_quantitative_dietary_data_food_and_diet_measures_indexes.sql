-- Indexes for MEASURES relationships from individual_quantitative_dietary_data_food_and_diet

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_measures_indicator_codes
ON fao_graph."MEASURES" USING btree ((properties->>'indicator_codes'));
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_measures_indicator
ON fao_graph."MEASURES" USING btree ((properties->>'indicator'));
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_measures_indicator_code
ON fao_graph."MEASURES" USING btree ((properties->>'indicator_code'));
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_measures_indicators
ON fao_graph."MEASURES" USING btree ((properties->>'indicators'));

-- Index on data properties


CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_measures_compound
ON fao_graph."MEASURES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_individual_quantitative_dietary_data_food_and_diet_measures_source
ON fao_graph."MEASURES" USING btree ((properties->>'source_dataset'));