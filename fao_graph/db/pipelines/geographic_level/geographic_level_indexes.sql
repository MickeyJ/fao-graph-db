-- Indexes for geographic_level nodes
CREATE INDEX IF NOT EXISTS idx_geographic_levels_geographic_level_code
ON fao.geographic_level USING btree ((properties->>'geographic_level_code'));

CREATE INDEX IF NOT EXISTS idx_geographic_levels_source_dataset  
ON fao.geographic_level USING btree ((properties->>'source_dataset'));

