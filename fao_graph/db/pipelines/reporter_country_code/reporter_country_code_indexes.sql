-- yaml_node_indexes.sql.jinja2
-- Indexes for ReporterCountryCode nodes
CREATE INDEX IF NOT EXISTS idx_reporter_country_codes_id
ON fao_graph."ReporterCountryCode" (id);


-- Compound index for node lookups
CREATE INDEX IF NOT EXISTS idx_reporter_country_codes_properties
ON fao_graph."ReporterCountryCode" USING GIN (properties);