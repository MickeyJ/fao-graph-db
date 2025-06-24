-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for EXPORTS relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_exports_unit 
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype])
);

-- Compound index for unit & year
CREATE INDEX IF NOT EXISTS idx_exports_unit_year
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

