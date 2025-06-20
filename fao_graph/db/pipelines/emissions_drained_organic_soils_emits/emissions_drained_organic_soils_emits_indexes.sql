-- Indexes for EMITS relationships from emissions_drained_organic_soils

CREATE INDEX IF NOT EXISTS idx_emissions_drained_organic_soils_emits_year
ON fao_graph."EMITS" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_emissions_drained_organic_soils_emits_value
ON fao_graph."EMITS" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_emissions_drained_organic_soils_emits_year_code
ON fao_graph."EMITS" USING btree ((properties->>'year_code'));
