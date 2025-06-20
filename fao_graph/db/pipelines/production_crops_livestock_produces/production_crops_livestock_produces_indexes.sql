-- Indexes for PRODUCES relationships from production_crops_livestock

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_production_crops_livestock_produces_measure
ON fao_graph."PRODUCES" USING btree ((properties->>'measure'));
CREATE INDEX IF NOT EXISTS idx_production_crops_livestock_produces_element_code
ON fao_graph."PRODUCES" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_production_crops_livestock_produces_element
ON fao_graph."PRODUCES" USING btree ((properties->>'element'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_production_crops_livestock_produces_year
ON fao_graph."PRODUCES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_production_crops_livestock_produces_value
ON fao_graph."PRODUCES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_production_crops_livestock_produces_compound
ON fao_graph."PRODUCES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_production_crops_livestock_produces_source
ON fao_graph."PRODUCES" USING btree ((properties->>'source_dataset'));