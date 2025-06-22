-- yaml_global_indexes.sql.jinja2
-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration

-- Indexes for TRADES relationships
CREATE INDEX IF NOT EXISTS idx_trades_source 
ON fao_graph."TRADES" (start_id);

CREATE INDEX IF NOT EXISTS idx_trades_target 
ON fao_graph."TRADES" (end_id);

CREATE INDEX IF NOT EXISTS idx_trades_year 
ON fao_graph."TRADES" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]));

CREATE INDEX IF NOT EXISTS idx_trades_source_dataset 
ON fao_graph."TRADES" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]));


-- Indexes for PRODUCES relationships
CREATE INDEX IF NOT EXISTS idx_produces_source 
ON fao_graph."PRODUCES" (start_id);

CREATE INDEX IF NOT EXISTS idx_produces_target 
ON fao_graph."PRODUCES" (end_id);

CREATE INDEX IF NOT EXISTS idx_produces_year 
ON fao_graph."PRODUCES" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]));

CREATE INDEX IF NOT EXISTS idx_produces_source_dataset 
ON fao_graph."PRODUCES" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]));


-- Indexes for CONSUMES relationships
CREATE INDEX IF NOT EXISTS idx_consumes_source 
ON fao_graph."CONSUMES" (start_id);

CREATE INDEX IF NOT EXISTS idx_consumes_target 
ON fao_graph."CONSUMES" (end_id);

CREATE INDEX IF NOT EXISTS idx_consumes_year 
ON fao_graph."CONSUMES" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]));

CREATE INDEX IF NOT EXISTS idx_consumes_source_dataset 
ON fao_graph."CONSUMES" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]));


-- Indexes for EXPERIENCES relationships
CREATE INDEX IF NOT EXISTS idx_experiences_source 
ON fao_graph."EXPERIENCES" (start_id);

CREATE INDEX IF NOT EXISTS idx_experiences_target 
ON fao_graph."EXPERIENCES" (end_id);

CREATE INDEX IF NOT EXISTS idx_experiences_year 
ON fao_graph."EXPERIENCES" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]));

CREATE INDEX IF NOT EXISTS idx_experiences_source_dataset 
ON fao_graph."EXPERIENCES" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]));


-- Indexes for MEASURES relationships
CREATE INDEX IF NOT EXISTS idx_measures_source 
ON fao_graph."MEASURES" (start_id);

CREATE INDEX IF NOT EXISTS idx_measures_target 
ON fao_graph."MEASURES" (end_id);

CREATE INDEX IF NOT EXISTS idx_measures_year 
ON fao_graph."MEASURES" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]));

CREATE INDEX IF NOT EXISTS idx_measures_source_dataset 
ON fao_graph."MEASURES" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]));


-- Indexes for HAS_PRICE relationships
CREATE INDEX IF NOT EXISTS idx_has_price_source 
ON fao_graph."HAS_PRICE" (start_id);

CREATE INDEX IF NOT EXISTS idx_has_price_target 
ON fao_graph."HAS_PRICE" (end_id);

CREATE INDEX IF NOT EXISTS idx_has_price_year 
ON fao_graph."HAS_PRICE" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]));

CREATE INDEX IF NOT EXISTS idx_has_price_source_dataset 
ON fao_graph."HAS_PRICE" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]));

-- Additional indexes for price queries
CREATE INDEX IF NOT EXISTS idx_has_price_months 
ON fao_graph."HAS_PRICE" USING btree (agtype_access_operator(VARIADIC ARRAY[properties, '"months_code"'::agtype]));


-- Compound indexes for common query patterns
CREATE INDEX IF NOT EXISTS idx_trades_year_source_compound 
ON fao_graph."TRADES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]),
    start_id,
    end_id
);
CREATE INDEX IF NOT EXISTS idx_produces_year_source_compound 
ON fao_graph."PRODUCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]),
    start_id,
    end_id
);
CREATE INDEX IF NOT EXISTS idx_consumes_year_source_compound 
ON fao_graph."CONSUMES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]),
    start_id,
    end_id
);
CREATE INDEX IF NOT EXISTS idx_experiences_year_source_compound 
ON fao_graph."EXPERIENCES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]),
    start_id,
    end_id
);
CREATE INDEX IF NOT EXISTS idx_measures_year_source_compound 
ON fao_graph."MEASURES" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]),
    start_id,
    end_id
);
CREATE INDEX IF NOT EXISTS idx_has_price_year_source_compound 
ON fao_graph."HAS_PRICE" USING btree (
    agtype_access_operator(VARIADIC ARRAY[properties, '"year"'::agtype]),
    agtype_access_operator(VARIADIC ARRAY[properties, '"source_dataset"'::agtype]),
    start_id,
    end_id
);

-- Alternative: GIN indexes for properties (choose one approach)
-- These are more flexible but may be less performant for specific property lookups
-- CREATE INDEX IF NOT EXISTS idx_trades_properties_gin 
-- ON fao_graph."TRADES" USING gin (properties);
-- CREATE INDEX IF NOT EXISTS idx_produces_properties_gin 
-- ON fao_graph."PRODUCES" USING gin (properties);
-- CREATE INDEX IF NOT EXISTS idx_consumes_properties_gin 
-- ON fao_graph."CONSUMES" USING gin (properties);
-- CREATE INDEX IF NOT EXISTS idx_experiences_properties_gin 
-- ON fao_graph."EXPERIENCES" USING gin (properties);
-- CREATE INDEX IF NOT EXISTS idx_measures_properties_gin 
-- ON fao_graph."MEASURES" USING gin (properties);
-- CREATE INDEX IF NOT EXISTS idx_has_price_properties_gin 
-- ON fao_graph."HAS_PRICE" USING gin (properties);
