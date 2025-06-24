-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for PRODUCES relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_produces_year 
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);


