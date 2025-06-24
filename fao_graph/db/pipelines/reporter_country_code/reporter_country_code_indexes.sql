-- yaml_node_indexes.sql.jinja2
-- Indexes for ReporterCountryCode nodes
CREATE INDEX IF NOT EXISTS idx_reporter_country_codes_id
ON fao_graph."ReporterCountryCode" (id);

CREATE INDEX IF NOT EXISTS idx_reporter_country_codes_reporter_country_code 
ON fao_graph."ReporterCountryCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"reporter_country_code"'::agtype])
);

-- Compound index for node lookups
CREATE INDEX IF NOT EXISTS idx_reporter_country_codes_properties
ON fao_graph."ReporterCountryCode" USING GIN (properties);