-- Strategic indexes for fao_graph graph database
-- Generated from YAML configuration


-- ============================================
-- Indexes for TRADES relationships
-- ============================================


-- Core relationship traversal indexes (start/end nodes)
CREATE INDEX IF NOT EXISTS idx_trades_source 
ON fao_graph."TRADES" (start_id);

CREATE INDEX IF NOT EXISTS idx_trades_target 
ON fao_graph."TRADES" (end_id);

-- Compound index for bidirectional traversal
CREATE INDEX IF NOT EXISTS idx_trades_source_target
ON fao_graph."TRADES" (start_id, end_id);
