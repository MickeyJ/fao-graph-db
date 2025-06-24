-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for EXPERIENCES relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_experiences_element_code 
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype])
);

-- Compound index for element_code & year
CREATE INDEX IF NOT EXISTS idx_experiences_element_code_year
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

