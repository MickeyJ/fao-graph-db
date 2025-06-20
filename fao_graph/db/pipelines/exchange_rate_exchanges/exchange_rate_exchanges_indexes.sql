-- Indexes for EXCHANGES relationships from exchange_rate

-- Index on relationship properties

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_exchange_rate_exchanges_year
ON fao_graph."EXCHANGES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_exchange_rate_exchanges_value
ON fao_graph."EXCHANGES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_exchange_rate_exchanges_compound
ON fao_graph."EXCHANGES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_exchange_rate_exchanges_source
ON fao_graph."EXCHANGES" USING btree ((properties->>'source_dataset'));