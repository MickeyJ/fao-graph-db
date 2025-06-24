-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for IMPORTS relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_imports_reporter_country_code 
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"reporter_country_code"'::agtype])
);

-- Compound index for reporter_country_code & year
CREATE INDEX IF NOT EXISTS idx_imports_reporter_country_code_year
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"reporter_country_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

