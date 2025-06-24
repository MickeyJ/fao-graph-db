-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


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
