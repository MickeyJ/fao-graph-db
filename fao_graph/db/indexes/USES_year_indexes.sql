-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for USES relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_uses_year 
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);


