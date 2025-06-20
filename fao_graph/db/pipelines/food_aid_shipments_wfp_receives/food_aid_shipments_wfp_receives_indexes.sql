-- Indexes for RECEIVES relationships from food_aid_shipments_wfp

-- Index on relationship properties

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_food_aid_shipments_wfp_receives_year
ON fao_graph."RECEIVES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_food_aid_shipments_wfp_receives_value
ON fao_graph."RECEIVES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_food_aid_shipments_wfp_receives_compound
ON fao_graph."RECEIVES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_food_aid_shipments_wfp_receives_source
ON fao_graph."RECEIVES" USING btree ((properties->>'source_dataset'));