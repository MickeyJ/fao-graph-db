-- Indexes for MEASURES relationships from investment_credit_agriculture

CREATE INDEX IF NOT EXISTS idx_investment_credit_agriculture_measures_year
ON fao_graph."MEASURES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_investment_credit_agriculture_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_investment_credit_agriculture_measures_year_code
ON fao_graph."MEASURES" USING btree ((properties->>'year_code'));
