-- yaml_node_indexes.sql.jinja2
-- Indexes for AreaCode nodes
CREATE INDEX IF NOT EXISTS idx_area_codes_id
ON fao_graph."AreaCode" (id);

CREATE INDEX IF NOT EXISTS idx_area_codes_area_code 
ON fao_graph."AreaCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"area_code"'::agtype])
);

-- Compound index for node lookups
CREATE INDEX IF NOT EXISTS idx_area_codes_properties
ON fao_graph."AreaCode" USING GIN (properties);