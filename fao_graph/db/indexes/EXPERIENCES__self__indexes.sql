-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


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
