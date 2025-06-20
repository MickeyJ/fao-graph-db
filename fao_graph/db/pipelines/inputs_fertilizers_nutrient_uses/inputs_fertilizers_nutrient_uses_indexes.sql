-- Indexes for USES relationships from inputs_fertilizers_nutrient

CREATE INDEX IF NOT EXISTS idx_inputs_fertilizers_nutrient_uses_year
ON fao_graph."USES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_inputs_fertilizers_nutrient_uses_value
ON fao_graph."USES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_inputs_fertilizers_nutrient_uses_year_code
ON fao_graph."USES" USING btree ((properties->>'year_code'));
