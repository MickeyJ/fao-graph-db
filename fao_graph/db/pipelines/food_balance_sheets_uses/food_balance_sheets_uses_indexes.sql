-- Indexes for USES relationships from food_balance_sheets

CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_uses_year
ON fao_graph."USES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_uses_value
ON fao_graph."USES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_food_balance_sheets_uses_year_code
ON fao_graph."USES" USING btree ((properties->>'year_code'));
