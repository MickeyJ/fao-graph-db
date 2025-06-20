-- Indexes for food_value nodes
CREATE INDEX IF NOT EXISTS idx_food_values_food_value_code
ON fao.food_value USING btree ((properties->>'food_value_code'));

CREATE INDEX IF NOT EXISTS idx_food_values_source_dataset  
ON fao.food_value USING btree ((properties->>'source_dataset'));

