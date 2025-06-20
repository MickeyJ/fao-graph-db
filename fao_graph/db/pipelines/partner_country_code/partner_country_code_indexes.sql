-- Indexes for partner_country_code nodes
CREATE INDEX IF NOT EXISTS idx_partner_country_codes_partner_country_code
ON fao.partner_country_code USING btree ((properties->>'partner_country_code'));

CREATE INDEX IF NOT EXISTS idx_partner_country_codes_source_dataset  
ON fao.partner_country_code USING btree ((properties->>'source_dataset'));

