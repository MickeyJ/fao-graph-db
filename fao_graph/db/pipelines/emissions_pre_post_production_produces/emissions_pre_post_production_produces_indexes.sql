-- Indexes for PRODUCES relationships from emissions_pre_post_production

CREATE INDEX IF NOT EXISTS idx_emissions_pre_post_production_produces_year
ON fao_graph."PRODUCES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_emissions_pre_post_production_produces_value
ON fao_graph."PRODUCES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_emissions_pre_post_production_produces_year_code
ON fao_graph."PRODUCES" USING btree ((properties->>'year_code'));
