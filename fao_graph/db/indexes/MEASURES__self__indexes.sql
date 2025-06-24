-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


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
