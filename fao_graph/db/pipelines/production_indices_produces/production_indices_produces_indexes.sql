-- Indexes for PRODUCES relationships from production_indices

CREATE INDEX IF NOT EXISTS idx_production_indices_produces_year
ON fao_graph."PRODUCES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_production_indices_produces_value
ON fao_graph."PRODUCES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_production_indices_produces_year_code
ON fao_graph."PRODUCES" USING btree ((properties->>'year_code'));
