-- Indexes for RECEIVES_FROM relationships from development_assistance_to_agriculture

CREATE INDEX IF NOT EXISTS idx_development_assistance_to_agriculture_receives_from_year
ON fao_graph."RECEIVES_FROM" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_development_assistance_to_agriculture_receives_from_value
ON fao_graph."RECEIVES_FROM" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_development_assistance_to_agriculture_receives_from_year_code
ON fao_graph."RECEIVES_FROM" USING btree ((properties->>'year_code'));
