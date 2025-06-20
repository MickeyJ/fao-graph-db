-- Indexes for element nodes
CREATE INDEX IF NOT EXISTS idx_elements_element_code
ON fao.element USING btree ((properties->>'element_code'));

CREATE INDEX IF NOT EXISTS idx_elements_source_dataset  
ON fao.element USING btree ((properties->>'source_dataset'));

