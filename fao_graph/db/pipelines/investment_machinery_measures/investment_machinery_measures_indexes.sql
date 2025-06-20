-- Indexes for MEASURES relationships from investment_machinery

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_investment_machinery_measures_category
ON fao_graph."MEASURES" USING btree ((properties->>'category'));
CREATE INDEX IF NOT EXISTS idx_investment_machinery_measures_flow_type
ON fao_graph."MEASURES" USING btree ((properties->>'flow_type'));
CREATE INDEX IF NOT EXISTS idx_investment_machinery_measures_element_code
ON fao_graph."MEASURES" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_investment_machinery_measures_element
ON fao_graph."MEASURES" USING btree ((properties->>'element'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_investment_machinery_measures_year
ON fao_graph."MEASURES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_investment_machinery_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_investment_machinery_measures_compound
ON fao_graph."MEASURES" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_investment_machinery_measures_source
ON fao_graph."MEASURES" USING btree ((properties->>'source_dataset'));