-- Indexes for MEASURES relationships from investment_foreign_direct_investment

CREATE INDEX IF NOT EXISTS idx_investment_foreign_direct_investment_measures_year
ON fao_graph."MEASURES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_investment_foreign_direct_investment_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_investment_foreign_direct_investment_measures_year_code
ON fao_graph."MEASURES" USING btree ((properties->>'year_code'));
