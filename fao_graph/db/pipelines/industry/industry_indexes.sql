-- Indexes for industry nodes
CREATE INDEX IF NOT EXISTS idx_industries_industry_code
ON fao.industry USING btree ((properties->>'industry_code'));

CREATE INDEX IF NOT EXISTS idx_industries_source_dataset  
ON fao.industry USING btree ((properties->>'source_dataset'));

