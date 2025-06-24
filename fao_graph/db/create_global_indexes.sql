-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration

-- ============================================
-- Indexes for PRODUCES relationships
-- ============================================

-- Core relationship traversal indexes (start/end nodes)
CREATE INDEX IF NOT EXISTS idx_produces_source 
ON fao_graph."PRODUCES" (start_id);

CREATE INDEX IF NOT EXISTS idx_produces_target 
ON fao_graph."PRODUCES" (end_id);

-- Compound index for bidirectional traversal
CREATE INDEX IF NOT EXISTS idx_produces_source_target
ON fao_graph."PRODUCES" (start_id, end_id);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_produces_element 
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype])
);

            
-- Compound index for element & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_element_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element & year
CREATE INDEX IF NOT EXISTS idx_produces_element_year
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_element_year_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_produces_element_code 
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype])
);

            
-- Compound index for element_code & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_element_code_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element_code & year
CREATE INDEX IF NOT EXISTS idx_produces_element_code_year
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element_code & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_element_code_year_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_produces_flag 
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype])
);

            
-- Compound index for flag & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_flag_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag & year
CREATE INDEX IF NOT EXISTS idx_produces_flag_year
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_flag_year_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_produces_flag_description 
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype])
);

            
-- Compound index for flag_description & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_flag_description_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag_description & year
CREATE INDEX IF NOT EXISTS idx_produces_flag_description_year
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag_description & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_flag_description_year_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_produces_note 
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype])
);

            
-- Compound index for note & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_note_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for note & year
CREATE INDEX IF NOT EXISTS idx_produces_note_year
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for note & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_note_year_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_produces_unit 
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype])
);

            
-- Compound index for unit & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_unit_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for unit & year
CREATE INDEX IF NOT EXISTS idx_produces_unit_year
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for unit & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_unit_year_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_produces_value 
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype])
);

            
-- Compound index for value & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_value_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for value & year
CREATE INDEX IF NOT EXISTS idx_produces_value_year
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for value & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_value_year_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_produces_year 
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

            
-- Compound index for year & source_dataset
CREATE INDEX IF NOT EXISTS idx_produces_year_dataset
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          



-- GIN index for flexible property searches (use sparingly due to write overhead)
-- Uncomment if needed for complex property queries
-- CREATE INDEX IF NOT EXISTS idx_produces_properties_gin
-- ON fao_graph."PRODUCES" USING GIN (properties);

-- ============================================
-- Indexes for EMITS relationships
-- ============================================

-- Core relationship traversal indexes (start/end nodes)
CREATE INDEX IF NOT EXISTS idx_emits_source 
ON fao_graph."EMITS" (start_id);

CREATE INDEX IF NOT EXISTS idx_emits_target 
ON fao_graph."EMITS" (end_id);

-- Compound index for bidirectional traversal
CREATE INDEX IF NOT EXISTS idx_emits_source_target
ON fao_graph."EMITS" (start_id, end_id);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_emits_element 
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype])
);

            
-- Compound index for element & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_element_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element & year
CREATE INDEX IF NOT EXISTS idx_emits_element_year
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_element_year_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_emits_element_code 
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype])
);

            
-- Compound index for element_code & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_element_code_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element_code & year
CREATE INDEX IF NOT EXISTS idx_emits_element_code_year
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element_code & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_element_code_year_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_emits_flag 
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype])
);

            
-- Compound index for flag & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_flag_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag & year
CREATE INDEX IF NOT EXISTS idx_emits_flag_year
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_flag_year_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_emits_flag_description 
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype])
);

            
-- Compound index for flag_description & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_flag_description_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag_description & year
CREATE INDEX IF NOT EXISTS idx_emits_flag_description_year
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag_description & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_flag_description_year_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_emits_unit 
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype])
);

            
-- Compound index for unit & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_unit_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for unit & year
CREATE INDEX IF NOT EXISTS idx_emits_unit_year
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for unit & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_unit_year_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_emits_value 
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype])
);

            
-- Compound index for value & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_value_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for value & year
CREATE INDEX IF NOT EXISTS idx_emits_value_year
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for value & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_value_year_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_emits_year 
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

            
-- Compound index for year & source_dataset
CREATE INDEX IF NOT EXISTS idx_emits_year_dataset
ON fao_graph."EMITS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          



-- GIN index for flexible property searches (use sparingly due to write overhead)
-- Uncomment if needed for complex property queries
-- CREATE INDEX IF NOT EXISTS idx_emits_properties_gin
-- ON fao_graph."EMITS" USING GIN (properties);

-- ============================================
-- Indexes for USES relationships
-- ============================================

-- Core relationship traversal indexes (start/end nodes)
CREATE INDEX IF NOT EXISTS idx_uses_source 
ON fao_graph."USES" (start_id);

CREATE INDEX IF NOT EXISTS idx_uses_target 
ON fao_graph."USES" (end_id);

-- Compound index for bidirectional traversal
CREATE INDEX IF NOT EXISTS idx_uses_source_target
ON fao_graph."USES" (start_id, end_id);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_uses_element 
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype])
);

            
-- Compound index for element & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_element_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element & year
CREATE INDEX IF NOT EXISTS idx_uses_element_year
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_element_year_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_uses_element_code 
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype])
);

            
-- Compound index for element_code & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_element_code_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element_code & year
CREATE INDEX IF NOT EXISTS idx_uses_element_code_year
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element_code & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_element_code_year_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_uses_flag 
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype])
);

            
-- Compound index for flag & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_flag_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag & year
CREATE INDEX IF NOT EXISTS idx_uses_flag_year
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_flag_year_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_uses_flag_description 
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype])
);

            
-- Compound index for flag_description & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_flag_description_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag_description & year
CREATE INDEX IF NOT EXISTS idx_uses_flag_description_year
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag_description & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_flag_description_year_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_uses_note 
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype])
);

            
-- Compound index for note & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_note_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for note & year
CREATE INDEX IF NOT EXISTS idx_uses_note_year
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for note & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_note_year_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_uses_unit 
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype])
);

            
-- Compound index for unit & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_unit_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for unit & year
CREATE INDEX IF NOT EXISTS idx_uses_unit_year
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for unit & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_unit_year_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_uses_value 
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype])
);

            
-- Compound index for value & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_value_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for value & year
CREATE INDEX IF NOT EXISTS idx_uses_value_year
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for value & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_value_year_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_uses_year 
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

            
-- Compound index for year & source_dataset
CREATE INDEX IF NOT EXISTS idx_uses_year_dataset
ON fao_graph."USES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          



-- GIN index for flexible property searches (use sparingly due to write overhead)
-- Uncomment if needed for complex property queries
-- CREATE INDEX IF NOT EXISTS idx_uses_properties_gin
-- ON fao_graph."USES" USING GIN (properties);

-- ============================================
-- Indexes for EXPORTS relationships
-- ============================================

-- Core relationship traversal indexes (start/end nodes)
CREATE INDEX IF NOT EXISTS idx_exports_source 
ON fao_graph."EXPORTS" (start_id);

CREATE INDEX IF NOT EXISTS idx_exports_target 
ON fao_graph."EXPORTS" (end_id);

-- Compound index for bidirectional traversal
CREATE INDEX IF NOT EXISTS idx_exports_source_target
ON fao_graph."EXPORTS" (start_id, end_id);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_exports_element 
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype])
);

            
-- Compound index for element & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_element_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element & year
CREATE INDEX IF NOT EXISTS idx_exports_element_year
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_element_year_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_exports_element_code 
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype])
);

            
-- Compound index for element_code & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_element_code_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element_code & year
CREATE INDEX IF NOT EXISTS idx_exports_element_code_year
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element_code & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_element_code_year_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_exports_flag 
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype])
);

            
-- Compound index for flag & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_flag_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag & year
CREATE INDEX IF NOT EXISTS idx_exports_flag_year
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_flag_year_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_exports_flag_description 
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype])
);

            
-- Compound index for flag_description & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_flag_description_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag_description & year
CREATE INDEX IF NOT EXISTS idx_exports_flag_description_year
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag_description & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_flag_description_year_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_exports_partner_countries 
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"partner_countries"'::agtype])
);

            
-- Compound index for partner_countries & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_partner_countries_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"partner_countries"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for partner_countries & year
CREATE INDEX IF NOT EXISTS idx_exports_partner_countries_year
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"partner_countries"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for partner_countries & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_partner_countries_year_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"partner_countries"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_exports_partner_country_code 
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"partner_country_code"'::agtype])
);

            
-- Compound index for partner_country_code & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_partner_country_code_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"partner_country_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for partner_country_code & year
CREATE INDEX IF NOT EXISTS idx_exports_partner_country_code_year
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"partner_country_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for partner_country_code & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_partner_country_code_year_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"partner_country_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_exports_unit 
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype])
);

            
-- Compound index for unit & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_unit_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for unit & year
CREATE INDEX IF NOT EXISTS idx_exports_unit_year
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for unit & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_unit_year_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_exports_value 
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype])
);

            
-- Compound index for value & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_value_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for value & year
CREATE INDEX IF NOT EXISTS idx_exports_value_year
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for value & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_value_year_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_exports_year 
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

            
-- Compound index for year & source_dataset
CREATE INDEX IF NOT EXISTS idx_exports_year_dataset
ON fao_graph."EXPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          



-- GIN index for flexible property searches (use sparingly due to write overhead)
-- Uncomment if needed for complex property queries
-- CREATE INDEX IF NOT EXISTS idx_exports_properties_gin
-- ON fao_graph."EXPORTS" USING GIN (properties);

-- ============================================
-- Indexes for IMPORTS relationships
-- ============================================

-- Core relationship traversal indexes (start/end nodes)
CREATE INDEX IF NOT EXISTS idx_imports_source 
ON fao_graph."IMPORTS" (start_id);

CREATE INDEX IF NOT EXISTS idx_imports_target 
ON fao_graph."IMPORTS" (end_id);

-- Compound index for bidirectional traversal
CREATE INDEX IF NOT EXISTS idx_imports_source_target
ON fao_graph."IMPORTS" (start_id, end_id);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_imports_element 
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype])
);

            
-- Compound index for element & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_element_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element & year
CREATE INDEX IF NOT EXISTS idx_imports_element_year
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_element_year_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_imports_element_code 
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype])
);

            
-- Compound index for element_code & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_element_code_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element_code & year
CREATE INDEX IF NOT EXISTS idx_imports_element_code_year
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element_code & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_element_code_year_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_imports_flag 
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype])
);

            
-- Compound index for flag & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_flag_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag & year
CREATE INDEX IF NOT EXISTS idx_imports_flag_year
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_flag_year_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_imports_flag_description 
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype])
);

            
-- Compound index for flag_description & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_flag_description_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag_description & year
CREATE INDEX IF NOT EXISTS idx_imports_flag_description_year
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag_description & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_flag_description_year_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_imports_reporter_countries 
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"reporter_countries"'::agtype])
);

            
-- Compound index for reporter_countries & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_reporter_countries_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"reporter_countries"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for reporter_countries & year
CREATE INDEX IF NOT EXISTS idx_imports_reporter_countries_year
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"reporter_countries"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for reporter_countries & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_reporter_countries_year_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"reporter_countries"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_imports_reporter_country_code 
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"reporter_country_code"'::agtype])
);

            
-- Compound index for reporter_country_code & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_reporter_country_code_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"reporter_country_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for reporter_country_code & year
CREATE INDEX IF NOT EXISTS idx_imports_reporter_country_code_year
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"reporter_country_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for reporter_country_code & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_reporter_country_code_year_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"reporter_country_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_imports_unit 
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype])
);

            
-- Compound index for unit & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_unit_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for unit & year
CREATE INDEX IF NOT EXISTS idx_imports_unit_year
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for unit & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_unit_year_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_imports_value 
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype])
);

            
-- Compound index for value & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_value_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for value & year
CREATE INDEX IF NOT EXISTS idx_imports_value_year
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for value & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_value_year_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_imports_year 
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

            
-- Compound index for year & source_dataset
CREATE INDEX IF NOT EXISTS idx_imports_year_dataset
ON fao_graph."IMPORTS" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          



-- GIN index for flexible property searches (use sparingly due to write overhead)
-- Uncomment if needed for complex property queries
-- CREATE INDEX IF NOT EXISTS idx_imports_properties_gin
-- ON fao_graph."IMPORTS" USING GIN (properties);

-- ============================================
-- Indexes for TRADES relationships
-- ============================================

-- Core relationship traversal indexes (start/end nodes)
CREATE INDEX IF NOT EXISTS idx_trades_source 
ON fao_graph."TRADES" (start_id);

CREATE INDEX IF NOT EXISTS idx_trades_target 
ON fao_graph."TRADES" (end_id);

-- Compound index for bidirectional traversal
CREATE INDEX IF NOT EXISTS idx_trades_source_target
ON fao_graph."TRADES" (start_id, end_id);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_trades_element 
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype])
);

            
-- Compound index for element & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_element_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element & year
CREATE INDEX IF NOT EXISTS idx_trades_element_year
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_element_year_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_trades_element_code 
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype])
);

            
-- Compound index for element_code & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_element_code_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element_code & year
CREATE INDEX IF NOT EXISTS idx_trades_element_code_year
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element_code & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_element_code_year_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_trades_flag 
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype])
);

            
-- Compound index for flag & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_flag_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag & year
CREATE INDEX IF NOT EXISTS idx_trades_flag_year
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_flag_year_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_trades_flag_description 
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype])
);

            
-- Compound index for flag_description & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_flag_description_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag_description & year
CREATE INDEX IF NOT EXISTS idx_trades_flag_description_year
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag_description & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_flag_description_year_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_trades_note 
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype])
);

            
-- Compound index for note & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_note_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for note & year
CREATE INDEX IF NOT EXISTS idx_trades_note_year
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for note & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_note_year_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_trades_unit 
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype])
);

            
-- Compound index for unit & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_unit_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for unit & year
CREATE INDEX IF NOT EXISTS idx_trades_unit_year
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for unit & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_unit_year_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_trades_value 
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype])
);

            
-- Compound index for value & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_value_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for value & year
CREATE INDEX IF NOT EXISTS idx_trades_value_year
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for value & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_value_year_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_trades_year 
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

            
-- Compound index for year & source_dataset
CREATE INDEX IF NOT EXISTS idx_trades_year_dataset
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          



-- GIN index for flexible property searches (use sparingly due to write overhead)
-- Uncomment if needed for complex property queries
-- CREATE INDEX IF NOT EXISTS idx_trades_properties_gin
-- ON fao_graph."TRADES" USING GIN (properties);

-- ============================================
-- Indexes for EXPERIENCES relationships
-- ============================================

-- Core relationship traversal indexes (start/end nodes)
CREATE INDEX IF NOT EXISTS idx_experiences_source 
ON fao_graph."EXPERIENCES" (start_id);

CREATE INDEX IF NOT EXISTS idx_experiences_target 
ON fao_graph."EXPERIENCES" (end_id);

-- Compound index for bidirectional traversal
CREATE INDEX IF NOT EXISTS idx_experiences_source_target
ON fao_graph."EXPERIENCES" (start_id, end_id);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_experiences_element 
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype])
);

            
-- Compound index for element & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_element_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element & year
CREATE INDEX IF NOT EXISTS idx_experiences_element_year
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_element_year_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_experiences_element_code 
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype])
);

            
-- Compound index for element_code & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_element_code_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element_code & year
CREATE INDEX IF NOT EXISTS idx_experiences_element_code_year
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element_code & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_element_code_year_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_experiences_flag 
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype])
);

            
-- Compound index for flag & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_flag_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag & year
CREATE INDEX IF NOT EXISTS idx_experiences_flag_year
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_flag_year_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_experiences_flag_description 
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype])
);

            
-- Compound index for flag_description & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_flag_description_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag_description & year
CREATE INDEX IF NOT EXISTS idx_experiences_flag_description_year
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag_description & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_flag_description_year_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_experiences_note 
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype])
);

            
-- Compound index for note & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_note_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for note & year
CREATE INDEX IF NOT EXISTS idx_experiences_note_year
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for note & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_note_year_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_experiences_unit 
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype])
);

            
-- Compound index for unit & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_unit_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for unit & year
CREATE INDEX IF NOT EXISTS idx_experiences_unit_year
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for unit & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_unit_year_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_experiences_value 
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype])
);

            
-- Compound index for value & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_value_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for value & year
CREATE INDEX IF NOT EXISTS idx_experiences_value_year
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for value & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_value_year_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_experiences_year 
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

            
-- Compound index for year & source_dataset
CREATE INDEX IF NOT EXISTS idx_experiences_year_dataset
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          



-- GIN index for flexible property searches (use sparingly due to write overhead)
-- Uncomment if needed for complex property queries
-- CREATE INDEX IF NOT EXISTS idx_experiences_properties_gin
-- ON fao_graph."EXPERIENCES" USING GIN (properties);

-- ============================================
-- Indexes for MEASURES relationships
-- ============================================

-- Core relationship traversal indexes (start/end nodes)
CREATE INDEX IF NOT EXISTS idx_measures_source 
ON fao_graph."MEASURES" (start_id);

CREATE INDEX IF NOT EXISTS idx_measures_target 
ON fao_graph."MEASURES" (end_id);

-- Compound index for bidirectional traversal
CREATE INDEX IF NOT EXISTS idx_measures_source_target
ON fao_graph."MEASURES" (start_id, end_id);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_measures_element 
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype])
);

            
-- Compound index for element & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_element_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element & year
CREATE INDEX IF NOT EXISTS idx_measures_element_year
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_element_year_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_measures_element_code 
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype])
);

            
-- Compound index for element_code & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_element_code_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element_code & year
CREATE INDEX IF NOT EXISTS idx_measures_element_code_year
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element_code & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_element_code_year_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_measures_flag 
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype])
);

            
-- Compound index for flag & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_flag_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag & year
CREATE INDEX IF NOT EXISTS idx_measures_flag_year
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_flag_year_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_measures_flag_description 
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype])
);

            
-- Compound index for flag_description & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_flag_description_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag_description & year
CREATE INDEX IF NOT EXISTS idx_measures_flag_description_year
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag_description & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_flag_description_year_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_measures_note 
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype])
);

            
-- Compound index for note & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_note_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for note & year
CREATE INDEX IF NOT EXISTS idx_measures_note_year
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for note & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_note_year_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"note"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_measures_unit 
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype])
);

            
-- Compound index for unit & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_unit_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for unit & year
CREATE INDEX IF NOT EXISTS idx_measures_unit_year
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for unit & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_unit_year_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_measures_value 
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype])
);

            
-- Compound index for value & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_value_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for value & year
CREATE INDEX IF NOT EXISTS idx_measures_value_year
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for value & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_value_year_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_measures_year 
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

            
-- Compound index for year & source_dataset
CREATE INDEX IF NOT EXISTS idx_measures_year_dataset
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          



-- GIN index for flexible property searches (use sparingly due to write overhead)
-- Uncomment if needed for complex property queries
-- CREATE INDEX IF NOT EXISTS idx_measures_properties_gin
-- ON fao_graph."MEASURES" USING GIN (properties);

-- ============================================
-- Indexes for HAS_PRICE relationships
-- ============================================

-- Core relationship traversal indexes (start/end nodes)
CREATE INDEX IF NOT EXISTS idx_has_price_source 
ON fao_graph."HAS_PRICE" (start_id);

CREATE INDEX IF NOT EXISTS idx_has_price_target 
ON fao_graph."HAS_PRICE" (end_id);

-- Compound index for bidirectional traversal
CREATE INDEX IF NOT EXISTS idx_has_price_source_target
ON fao_graph."HAS_PRICE" (start_id, end_id);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_has_price_element 
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype])
);

            
-- Compound index for element & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_element_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element & year
CREATE INDEX IF NOT EXISTS idx_has_price_element_year
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_element_year_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_has_price_element_code 
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype])
);

            
-- Compound index for element_code & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_element_code_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for element_code & year
CREATE INDEX IF NOT EXISTS idx_has_price_element_code_year
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for element_code & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_element_code_year_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"element_code"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_has_price_flag 
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype])
);

            
-- Compound index for flag & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_flag_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag & year
CREATE INDEX IF NOT EXISTS idx_has_price_flag_year
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_flag_year_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_has_price_flag_description 
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype])
);

            
-- Compound index for flag_description & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_flag_description_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for flag_description & year
CREATE INDEX IF NOT EXISTS idx_has_price_flag_description_year
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for flag_description & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_flag_description_year_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"flag_description"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_has_price_months 
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"months"'::agtype])
);

            
-- Compound index for months & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_months_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"months"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for months & year
CREATE INDEX IF NOT EXISTS idx_has_price_months_year
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"months"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for months & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_months_year_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"months"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_has_price_unit 
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype])
);

            
-- Compound index for unit & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_unit_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for unit & year
CREATE INDEX IF NOT EXISTS idx_has_price_unit_year
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for unit & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_unit_year_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"unit"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_has_price_value 
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype])
);

            
-- Compound index for value & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_value_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          

-- Compound index for value & year
CREATE INDEX IF NOT EXISTS idx_has_price_value_year
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);
-- Compound index for value & year & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_value_year_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"value"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);


-- Property-specific BTREE indexes for efficient filtering
CREATE INDEX IF NOT EXISTS idx_has_price_year 
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype])
);

            
-- Compound index for year & source_dataset
CREATE INDEX IF NOT EXISTS idx_has_price_year_dataset
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype])
);
          



-- GIN index for flexible property searches (use sparingly due to write overhead)
-- Uncomment if needed for complex property queries
-- CREATE INDEX IF NOT EXISTS idx_has_price_properties_gin
-- ON fao_graph."HAS_PRICE" USING GIN (properties);


-- ============================================
-- Performance optimization recommendations
-- ============================================
-- After creating indexes, run:
-- ANALYZE fao_graph._ag_label_vertex;
-- ANALYZE fao_graph._ag_label_edge;
-- ANALYZE fao_graph."PRODUCES";
-- ANALYZE fao_graph."EMITS";
-- ANALYZE fao_graph."USES";
-- ANALYZE fao_graph."EXPORTS";
-- ANALYZE fao_graph."IMPORTS";
-- ANALYZE fao_graph."TRADES";
-- ANALYZE fao_graph."EXPERIENCES";
-- ANALYZE fao_graph."MEASURES";
-- ANALYZE fao_graph."HAS_PRICE";

-- Monitor index usage with:
-- SELECT schemaname, tablename, indexname, idx_scan, idx_tup_read, idx_tup_fetch
-- FROM pg_stat_user_indexes
-- WHERE schemaname = 'fao_graph'
-- ORDER BY idx_scan;