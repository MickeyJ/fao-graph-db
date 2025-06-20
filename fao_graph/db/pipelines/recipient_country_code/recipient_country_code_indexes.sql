-- Indexes for recipient_country_code nodes
CREATE INDEX IF NOT EXISTS idx_recipient_country_codes_recipient_country_code
ON fao.recipient_country_code USING btree ((properties->>'recipient_country_code'));

CREATE INDEX IF NOT EXISTS idx_recipient_country_codes_source_dataset  
ON fao.recipient_country_code USING btree ((properties->>'source_dataset'));

