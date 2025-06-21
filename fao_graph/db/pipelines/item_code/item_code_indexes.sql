-- yaml_node_indexes.sql.jinja2
-- Indexes for ItemCode nodes
CREATE INDEX IF NOT EXISTS idx_item_codes_id
ON fao_graph."ItemCode" (id);


-- Compound index for node lookups
CREATE INDEX IF NOT EXISTS idx_item_codes_properties
ON fao_graph."ItemCode" USING GIN (properties);