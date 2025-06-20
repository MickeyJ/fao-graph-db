-- Indexes for PRODUCES relationships from food_balance_sheets

CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_produces_year
ON fao_graph."PRODUCES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_produces_value
ON fao_graph."PRODUCES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_produces_year_code
ON fao_graph."PRODUCES" USING btree ((properties->>'year_code'));
