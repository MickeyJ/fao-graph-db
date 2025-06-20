-- Indexes for source nodes
CREATE INDEX IF NOT EXISTS idx_sources_source_code
ON fao.source USING btree ((properties->>'source_code'));

CREATE INDEX IF NOT EXISTS idx_sources_source_dataset  
ON fao.source USING btree ((properties->>'source_dataset'));

