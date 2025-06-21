-- Indexes for SUPPLIES relationships from supply_utilization_accounts_food_and_diet

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_supply_utilization_accounts_food_and_diet_supplies_indicator_codes
ON fao_graph."SUPPLIES" USING btree ((properties->>'indicator_codes'));
CREATE INDEX IF NOT EXISTS idx_supply_utilization_accounts_food_and_diet_supplies_indicator
ON fao_graph."SUPPLIES" USING btree ((properties->>'indicator'));
CREATE INDEX IF NOT EXISTS idx_supply_utilization_accounts_food_and_diet_supplies_indicator_code
ON fao_graph."SUPPLIES" USING btree ((properties->>'indicator_code'));
CREATE INDEX IF NOT EXISTS idx_supply_utilization_accounts_food_and_diet_supplies_indicators
ON fao_graph."SUPPLIES" USING btree ((properties->>'indicators'));
CREATE INDEX IF NOT EXISTS idx_supply_utilization_accounts_food_and_diet_supplies_nutrient_type
ON fao_graph."SUPPLIES" USING btree ((properties->>'nutrient_type'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_supply_utilization_accounts_food_and_diet_supplies_year
ON fao_graph."SUPPLIES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_supply_utilization_accounts_food_and_diet_supplies_value
ON fao_graph."SUPPLIES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_supply_utilization_accounts_food_and_diet_supplies_compound
ON fao_graph."SUPPLIES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_supply_utilization_accounts_food_and_diet_supplies_source
ON fao_graph."SUPPLIES" USING btree ((properties->>'source_dataset'));