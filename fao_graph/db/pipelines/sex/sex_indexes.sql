-- Indexes for sex nodes
CREATE INDEX IF NOT EXISTS idx_sexs_sex_code
ON fao.sex USING btree ((properties->>'sex_code'));

CREATE INDEX IF NOT EXISTS idx_sexs_source_dataset  
ON fao.sex USING btree ((properties->>'source_dataset'));

