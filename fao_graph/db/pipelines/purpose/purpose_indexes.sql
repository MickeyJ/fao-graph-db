-- Indexes for purpose nodes
CREATE INDEX IF NOT EXISTS idx_purposes_purpose_code
ON fao.purpose USING btree ((properties->>'purpose_code'));

CREATE INDEX IF NOT EXISTS idx_purposes_source_dataset  
ON fao.purpose USING btree ((properties->>'source_dataset'));

