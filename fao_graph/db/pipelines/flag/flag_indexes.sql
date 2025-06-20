-- Indexes for flag nodes
CREATE INDEX IF NOT EXISTS idx_flags_flag
ON fao.flag USING btree ((properties->>'flag'));

CREATE INDEX IF NOT EXISTS idx_flags_source_dataset  
ON fao.flag USING btree ((properties->>'source_dataset'));

