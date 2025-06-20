-- Indexes for factor nodes
CREATE INDEX IF NOT EXISTS idx_factors_factor_code
ON fao.factor USING btree ((properties->>'factor_code'));

CREATE INDEX IF NOT EXISTS idx_factors_source_dataset  
ON fao.factor USING btree ((properties->>'source_dataset'));

