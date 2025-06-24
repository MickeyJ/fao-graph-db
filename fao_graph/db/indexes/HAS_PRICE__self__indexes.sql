-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


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
