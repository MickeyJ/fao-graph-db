-- Indexes for USES relationships from inputs_pesticides_use

CREATE INDEX IF NOT EXISTS idx_inputs_pesticides_use_uses_year
ON fao_graph."USES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_inputs_pesticides_use_uses_value
ON fao_graph."USES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_inputs_pesticides_use_uses_year_code
ON fao_graph."USES" USING btree ((properties->>'year_code'));
