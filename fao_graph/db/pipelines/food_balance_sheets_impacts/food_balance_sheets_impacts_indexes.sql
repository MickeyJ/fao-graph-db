-- Indexes for IMPACTS relationships from food_balance_sheets

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_impacts_element_codes
ON fao_graph."IMPACTS" USING btree ((properties->>'element_codes'));
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_impacts_element
ON fao_graph."IMPACTS" USING btree ((properties->>'element'));
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_impacts_element_code
ON fao_graph."IMPACTS" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_impacts_elements
ON fao_graph."IMPACTS" USING btree ((properties->>'elements'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_impacts_year
ON fao_graph."IMPACTS" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_impacts_value
ON fao_graph."IMPACTS" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_impacts_compound
ON fao_graph."IMPACTS" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_impacts_source
ON fao_graph."IMPACTS" USING btree ((properties->>'source_dataset'));