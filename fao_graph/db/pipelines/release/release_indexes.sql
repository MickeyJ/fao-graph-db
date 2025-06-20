-- Indexes for release nodes
CREATE INDEX IF NOT EXISTS idx_releases_release_code
ON fao.release USING btree ((properties->>'release_code'));

CREATE INDEX IF NOT EXISTS idx_releases_source_dataset  
ON fao.release USING btree ((properties->>'source_dataset'));

