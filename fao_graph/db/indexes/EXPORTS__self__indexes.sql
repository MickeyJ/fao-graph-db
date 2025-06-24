-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


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
