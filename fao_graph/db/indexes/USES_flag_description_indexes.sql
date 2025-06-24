-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for USES relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_uses_flag_description 
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype])
);

-- Compound index for flag_description & year
CREATE INDEX IF NOT EXISTS idx_uses_flag_description_year
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

