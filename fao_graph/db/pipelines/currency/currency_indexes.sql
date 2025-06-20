-- Indexes for currency nodes
CREATE INDEX IF NOT EXISTS idx_currencies_iso_currency_code
ON fao.currency USING btree ((properties->>'iso_currency_code'));

CREATE INDEX IF NOT EXISTS idx_currencies_source_dataset  
ON fao.currency USING btree ((properties->>'source_dataset'));

