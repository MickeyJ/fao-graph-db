-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for EXPERIENCES relationships
-- ============================================



-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_experiences_note 
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype])
);

-- Compound index for note & year
CREATE INDEX IF NOT EXISTS idx_experiences_note_year
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

