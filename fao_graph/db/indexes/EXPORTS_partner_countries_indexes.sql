-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for EXPORTS relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_exports_partner_countries 
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"partner_countries"'::agtype])
);

-- Compound index for partner_countries & year
CREATE INDEX IF NOT EXISTS idx_exports_partner_countries_year
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"partner_countries"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

