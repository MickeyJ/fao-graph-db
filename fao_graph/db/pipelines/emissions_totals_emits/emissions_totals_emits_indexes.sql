-- Indexes for EMITS relationships from emissions_totals

CREATE INDEX IF NOT EXISTS idx_emissions_totals_emits_year
ON fao_graph."EMITS" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_emissions_totals_emits_value
ON fao_graph."EMITS" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_emissions_totals_emits_year_code
ON fao_graph."EMITS" USING btree ((properties->>'year_code'));
