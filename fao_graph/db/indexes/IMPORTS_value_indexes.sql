-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for IMPORTS relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_imports_value 
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype])
);

-- Compound index for value & year
CREATE INDEX IF NOT EXISTS idx_imports_value_year
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

