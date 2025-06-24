-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for IMPORTS relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_imports_element 
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype])
);

-- Compound index for element & year
CREATE INDEX IF NOT EXISTS idx_imports_element_year
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

