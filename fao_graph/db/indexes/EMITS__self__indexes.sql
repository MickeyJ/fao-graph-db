-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


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
