-- yaml_node_indexes.sql.jinja2
-- Indexes for AreaCode nodes
CREATE INDEX IF NOT EXISTS idx_area_codes_id
ON fao_graph.'AreaCode' (id);


-- Compound index for node lookups
CREATE INDEX IF NOT EXISTS idx_area_codes_properties
ON fao_graph.'AreaCode' USING GIN (properties);