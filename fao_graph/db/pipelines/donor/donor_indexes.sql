-- Indexes for donor nodes
CREATE INDEX IF NOT EXISTS idx_donors_donor_code
ON fao.donor USING btree ((properties->>'donor_code'));

CREATE INDEX IF NOT EXISTS idx_donors_source_dataset  
ON fao.donor USING btree ((properties->>'source_dataset'));

