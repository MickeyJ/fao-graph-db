-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for MEASURES relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_measures_year 
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);


