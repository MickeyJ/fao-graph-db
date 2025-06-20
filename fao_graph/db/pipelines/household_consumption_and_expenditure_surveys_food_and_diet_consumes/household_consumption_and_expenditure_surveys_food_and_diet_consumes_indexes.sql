-- Indexes for CONSUMES relationships from household_consumption_and_expenditure_surveys_food_and_diet

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_household_consumption_and_expenditure_surveys_food_and_diet_consumes_indicator_codes
ON fao_graph."CONSUMES" USING btree ((properties->>'indicator_codes'));
CREATE INDEX IF NOT EXISTS idx_household_consumption_and_expenditure_surveys_food_and_diet_consumes_indicator
ON fao_graph."CONSUMES" USING btree ((properties->>'indicator'));
CREATE INDEX IF NOT EXISTS idx_household_consumption_and_expenditure_surveys_food_and_diet_consumes_indicator_code
ON fao_graph."CONSUMES" USING btree ((properties->>'indicator_code'));

-- Index on data properties


CREATE INDEX IF NOT EXISTS idx_household_consumption_and_expenditure_surveys_food_and_diet_consumes_value
ON fao_graph."CONSUMES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_household_consumption_and_expenditure_surveys_food_and_diet_consumes_compound
ON fao_graph."CONSUMES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_household_consumption_and_expenditure_surveys_food_and_diet_consumes_source
ON fao_graph."CONSUMES" USING btree ((properties->>'source_dataset'));