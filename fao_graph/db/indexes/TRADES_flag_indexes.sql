-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for TRADES relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_trades_flag 
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype])
);

-- Compound index for flag & year
CREATE INDEX IF NOT EXISTS idx_trades_flag_year
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

