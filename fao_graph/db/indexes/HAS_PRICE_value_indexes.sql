-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for HAS_PRICE relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_has_price_value 
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype])
);

-- Compound index for value & year
CREATE INDEX IF NOT EXISTS idx_has_price_value_year
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

