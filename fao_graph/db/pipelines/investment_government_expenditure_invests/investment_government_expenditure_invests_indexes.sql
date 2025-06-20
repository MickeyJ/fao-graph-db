-- Indexes for INVESTS relationships from investment_government_expenditure

-- Index on relationship properties
CREATE INDEX IF NOT EXISTS idx_investment_government_expenditure_invests_measure
ON fao_graph."INVESTS" USING btree ((properties->>'measure'));
CREATE INDEX IF NOT EXISTS idx_investment_government_expenditure_invests_currency
ON fao_graph."INVESTS" USING btree ((properties->>'currency'));
CREATE INDEX IF NOT EXISTS idx_investment_government_expenditure_invests_element_code
ON fao_graph."INVESTS" USING btree ((properties->>'element_code'));
CREATE INDEX IF NOT EXISTS idx_investment_government_expenditure_invests_element
ON fao_graph."INVESTS" USING btree ((properties->>'element'));

-- Index on data properties
CREATE INDEX IF NOT EXISTS idx_investment_government_expenditure_invests_year
ON fao_graph."INVESTS" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_investment_government_expenditure_invests_value
ON fao_graph."INVESTS" USING btree ((properties->>'value'));

-- Compound index for common query patterns
CREATE INDEX IF NOT EXISTS idx_investment_government_expenditure_invests_compound
ON fao_graph."INVESTS" USING GIN (properties);

-- Source dataset index for filtering
CREATE INDEX IF NOT EXISTS idx_investment_government_expenditure_invests_source
ON fao_graph."INVESTS" USING btree ((properties->>'source_dataset'));