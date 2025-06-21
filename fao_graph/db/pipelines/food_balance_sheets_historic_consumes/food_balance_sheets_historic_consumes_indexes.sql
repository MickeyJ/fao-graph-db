-- Indexes for CONSUMES relationships from food_balance_sheets_historic

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_historic_consumes_element_codes
ON fao_graph."CONSUMES" USING btree ((properties->>'element_codes'));
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_historic_consumes_element
ON fao_graph."CONSUMES" USING btree ((properties->>'element'));
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_historic_consumes_element_code
ON fao_graph."CONSUMES" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_historic_consumes_elements
ON fao_graph."CONSUMES" USING btree ((properties->>'elements'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_historic_consumes_year
ON fao_graph."CONSUMES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_historic_consumes_value
ON fao_graph."CONSUMES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_historic_consumes_compound
ON fao_graph."CONSUMES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_historic_consumes_source
ON fao_graph."CONSUMES" USING btree ((properties->>'source_dataset'));