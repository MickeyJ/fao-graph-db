-- Indexes for SUPPLIES relationships from food_balance_sheets

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_supplies_nutrient
ON fao_graph."SUPPLIES" USING btree ((properties->>'nutrient'));
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_supplies_measure
ON fao_graph."SUPPLIES" USING btree ((properties->>'measure'));
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_supplies_unit
ON fao_graph."SUPPLIES" USING btree ((properties->>'unit'));
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_supplies_element_code
ON fao_graph."SUPPLIES" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_supplies_element
ON fao_graph."SUPPLIES" USING btree ((properties->>'element'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_supplies_year
ON fao_graph."SUPPLIES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_supplies_value
ON fao_graph."SUPPLIES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_supplies_compound
ON fao_graph."SUPPLIES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_supplies_source
ON fao_graph."SUPPLIES" USING btree ((properties->>'source_dataset'));