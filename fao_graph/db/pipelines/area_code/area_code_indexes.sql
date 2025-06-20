-- Indexes for area_code nodes
CREATE INDEX IF NOT EXISTS idx_area_codes_area_code
ON fao.area_code USING btree ((properties->>'area_code'));

CREATE INDEX IF NOT EXISTS idx_area_codes_source_dataset  
ON fao.area_code USING btree ((properties->>'source_dataset'));

