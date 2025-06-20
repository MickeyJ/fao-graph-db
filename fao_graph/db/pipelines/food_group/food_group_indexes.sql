-- Indexes for food_group nodes
CREATE INDEX IF NOT EXISTS idx_food_groups_food_group_code
ON fao.food_group USING btree ((properties->>'food_group_code'));

CREATE INDEX IF NOT EXISTS idx_food_groups_source_dataset  
ON fao.food_group USING btree ((properties->>'source_dataset'));

