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
