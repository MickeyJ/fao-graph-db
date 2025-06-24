-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for TRADES relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_trades_unit 
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype])
);

-- Compound index for unit & year
CREATE INDEX IF NOT EXISTS idx_trades_unit_year
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

