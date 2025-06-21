-- yaml_global_indexes.sql.jinja2
-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration

-- Indexes for TRADES relationships
CREATE INDEX IF NOT EXISTS idx_trades_source 
ON fao_graph.trades (start_id);

CREATE INDEX IF NOT EXISTS idx_trades_target 
ON fao_graph.trades (end_id);

CREATE INDEX IF NOT EXISTS idx_trades_year 
ON fao_graph.trades USING btree ((properties->>'year'));

CREATE INDEX IF NOT EXISTS idx_trades_source_dataset 
ON fao_graph.trades USING btree ((properties->>'source_dataset'));


-- Indexes for PRODUCES relationships
CREATE INDEX IF NOT EXISTS idx_produces_source 
ON fao_graph.produces (start_id);

CREATE INDEX IF NOT EXISTS idx_produces_target 
ON fao_graph.produces (end_id);

CREATE INDEX IF NOT EXISTS idx_produces_year 
ON fao_graph.produces USING btree ((properties->>'year'));

CREATE INDEX IF NOT EXISTS idx_produces_source_dataset 
ON fao_graph.produces USING btree ((properties->>'source_dataset'));


-- Indexes for CONSUMES relationships
CREATE INDEX IF NOT EXISTS idx_consumes_source 
ON fao_graph.consumes (start_id);

CREATE INDEX IF NOT EXISTS idx_consumes_target 
ON fao_graph.consumes (end_id);

CREATE INDEX IF NOT EXISTS idx_consumes_year 
ON fao_graph.consumes USING btree ((properties->>'year'));

CREATE INDEX IF NOT EXISTS idx_consumes_source_dataset 
ON fao_graph.consumes USING btree ((properties->>'source_dataset'));


-- Indexes for EXPERIENCES relationships
CREATE INDEX IF NOT EXISTS idx_experiences_source 
ON fao_graph.experiences (start_id);

CREATE INDEX IF NOT EXISTS idx_experiences_target 
ON fao_graph.experiences (end_id);

CREATE INDEX IF NOT EXISTS idx_experiences_year 
ON fao_graph.experiences USING btree ((properties->>'year'));

CREATE INDEX IF NOT EXISTS idx_experiences_source_dataset 
ON fao_graph.experiences USING btree ((properties->>'source_dataset'));


-- Indexes for MEASURES relationships
CREATE INDEX IF NOT EXISTS idx_measures_source 
ON fao_graph.measures (start_id);

CREATE INDEX IF NOT EXISTS idx_measures_target 
ON fao_graph.measures (end_id);

CREATE INDEX IF NOT EXISTS idx_measures_year 
ON fao_graph.measures USING btree ((properties->>'year'));

CREATE INDEX IF NOT EXISTS idx_measures_source_dataset 
ON fao_graph.measures USING btree ((properties->>'source_dataset'));


-- Indexes for HAS_PRICE relationships
CREATE INDEX IF NOT EXISTS idx_has_price_source 
ON fao_graph.has_price (start_id);

CREATE INDEX IF NOT EXISTS idx_has_price_target 
ON fao_graph.has_price (end_id);

CREATE INDEX IF NOT EXISTS idx_has_price_year 
ON fao_graph.has_price USING btree ((properties->>'year'));

CREATE INDEX IF NOT EXISTS idx_has_price_source_dataset 
ON fao_graph.has_price USING btree ((properties->>'source_dataset'));

-- Additional indexes for price queries
CREATE INDEX IF NOT EXISTS idx_has_price_months 
ON fao_graph.has_price USING btree ((properties->>'months_code'));


-- Compound indexes for common query patterns
CREATE INDEX IF NOT EXISTS idx_trades_year_source 
ON fao_graph.trades USING btree (
    (properties->>'year'),
    (properties->>'source_dataset'),
    start_id,
    end_id
);
CREATE INDEX IF NOT EXISTS idx_produces_year_source 
ON fao_graph.produces USING btree (
    (properties->>'year'),
    (properties->>'source_dataset'),
    start_id,
    end_id
);
CREATE INDEX IF NOT EXISTS idx_consumes_year_source 
ON fao_graph.consumes USING btree (
    (properties->>'year'),
    (properties->>'source_dataset'),
    start_id,
    end_id
);
CREATE INDEX IF NOT EXISTS idx_experiences_year_source 
ON fao_graph.experiences USING btree (
    (properties->>'year'),
    (properties->>'source_dataset'),
    start_id,
    end_id
);
CREATE INDEX IF NOT EXISTS idx_measures_year_source 
ON fao_graph.measures USING btree (
    (properties->>'year'),
    (properties->>'source_dataset'),
    start_id,
    end_id
);
CREATE INDEX IF NOT EXISTS idx_has_price_year_source 
ON fao_graph.has_price USING btree (
    (properties->>'year'),
    (properties->>'source_dataset'),
    start_id,
    end_id
);
