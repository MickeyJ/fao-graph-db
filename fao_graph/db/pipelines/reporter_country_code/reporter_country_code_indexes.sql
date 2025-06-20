-- Indexes for reporter_country_code nodes
CREATE INDEX IF NOT EXISTS idx_reporter_country_codes_reporter_country_code
ON fao.reporter_country_code USING btree ((properties->>'reporter_country_code'));

CREATE INDEX IF NOT EXISTS idx_reporter_country_codes_source_dataset  
ON fao.reporter_country_code USING btree ((properties->>'source_dataset'));

