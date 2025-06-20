-- Indexes for item_code nodes
CREATE INDEX IF NOT EXISTS idx_item_codes_item_code
ON fao.item_code USING btree ((properties->>'item_code'));

CREATE INDEX IF NOT EXISTS idx_item_codes_source_dataset  
ON fao.item_code USING btree ((properties->>'source_dataset'));

