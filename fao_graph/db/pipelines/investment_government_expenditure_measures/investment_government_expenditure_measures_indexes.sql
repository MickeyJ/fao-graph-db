-- Indexes for MEASURES relationships from investment_government_expenditure

CREATE INDEX IF NOT EXISTS idx_investment_government_expenditure_measures_year
ON fao_graph."MEASURES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_investment_government_expenditure_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_investment_government_expenditure_measures_year_code
ON fao_graph."MEASURES" USING btree ((properties->>'year_code'));
