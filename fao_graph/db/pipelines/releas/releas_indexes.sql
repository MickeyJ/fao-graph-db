-- Indexes for releas nodes
CREATE INDEX IF NOT EXISTS idx_releases_release_code
ON fao.releas USING btree ((properties->>'release_code'));

CREATE INDEX IF NOT EXISTS idx_releases_source_dataset  
ON fao.releas USING btree ((properties->>'source_dataset'));

