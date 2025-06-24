-- yaml_node_indexes.sql.jinja2
-- Indexes for ReporterCountryCode nodes
CREATE INDEX IF NOT EXISTS idx_reporter_country_codes_id
ON fao_graph."ReporterCountryCode" (id);

CREATE INDEX IF NOT EXISTS idx_reporter_country_codes_reporter_country_code 
ON fao_graph."ReporterCountryCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"reporter_country_code"'::agtype])
);

CREATE INDEX IF NOT EXISTS idx_reporter_country_codes_sd_trade_detailed_trade_matrix
ON fao_graph."ReporterCountryCode" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
)
WHERE agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]) = '"trade_detailed_trade_matrix"'::agtype;



-- Compound index for node lookups
CREATE INDEX IF NOT EXISTS idx_reporter_country_codes_properties
ON fao_graph."ReporterCountryCode" USING GIN (properties);