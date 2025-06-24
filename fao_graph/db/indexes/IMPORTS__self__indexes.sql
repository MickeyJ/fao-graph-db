-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


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
