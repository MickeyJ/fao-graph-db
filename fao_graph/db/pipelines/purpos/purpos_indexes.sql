-- Indexes for purpos nodes
CREATE INDEX IF NOT EXISTS idx_purposes_purpose_code
ON fao.purpos USING btree ((properties->>'purpose_code'));

CREATE INDEX IF NOT EXISTS idx_purposes_source_dataset  
ON fao.purpos USING btree ((properties->>'source_dataset'));

