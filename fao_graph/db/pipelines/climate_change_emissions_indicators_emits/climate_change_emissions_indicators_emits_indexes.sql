-- Indexes for EMITS relationships from climate_change_emissions_indicators

CREATE INDEX IF NOT EXISTS idx_climate_change_emissions_indicators_emits_year
ON fao_graph."EMITS" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_climate_change_emissions_indicators_emits_value
ON fao_graph."EMITS" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_climate_change_emissions_indicators_emits_year_code
ON fao_graph."EMITS" USING btree ((properties->>'year_code'));
