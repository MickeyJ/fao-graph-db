-- Indexes for EMPLOYS relationships from asti_researchers

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_asti_researchers_employs_role
ON fao_graph."EMPLOYS" USING btree ((properties->>'role'));
CREATE INDEX IF NOT EXISTS idx_asti_researchers_employs_measure
ON fao_graph."EMPLOYS" USING btree ((properties->>'measure'));
CREATE INDEX IF NOT EXISTS idx_asti_researchers_employs_element_code
ON fao_graph."EMPLOYS" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_asti_researchers_employs_element
ON fao_graph."EMPLOYS" USING btree ((properties->>'element'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_asti_researchers_employs_year
ON fao_graph."EMPLOYS" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_asti_researchers_employs_value
ON fao_graph."EMPLOYS" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_asti_researchers_employs_compound
ON fao_graph."EMPLOYS" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_asti_researchers_employs_source
ON fao_graph."EMPLOYS" USING btree ((properties->>'source_dataset'));