-- Indexes for USES relationships from sua_crops_livestock

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_sua_crops_livestock_uses_resource
ON fao_graph."USES" USING btree ((properties->>'resource'));
CREATE INDEX IF NOT EXISTS idx_sua_crops_livestock_uses_purpose
ON fao_graph."USES" USING btree ((properties->>'purpose'));
CREATE INDEX IF NOT EXISTS idx_sua_crops_livestock_uses_element_code
ON fao_graph."USES" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_sua_crops_livestock_uses_element
ON fao_graph."USES" USING btree ((properties->>'element'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_sua_crops_livestock_uses_year
ON fao_graph."USES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_sua_crops_livestock_uses_value
ON fao_graph."USES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_sua_crops_livestock_uses_compound
ON fao_graph."USES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_sua_crops_livestock_uses_source
ON fao_graph."USES" USING btree ((properties->>'source_dataset'));