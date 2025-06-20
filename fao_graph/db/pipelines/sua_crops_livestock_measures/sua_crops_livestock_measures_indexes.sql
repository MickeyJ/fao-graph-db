-- Indexes for MEASURES relationships from sua_crops_livestock

CREATE INDEX IF NOT EXISTS idx_sua_crops_livestock_measures_year
ON fao_graph."MEASURES" USING btree ((properties->>'year'));


CREATE INDEX IF NOT EXISTS idx_sua_crops_livestock_measures_value
ON fao_graph."MEASURES" USING btree ((properties->>'value'));

CREATE INDEX IF NOT EXISTS idx_sua_crops_livestock_measures_year_code
ON fao_graph."MEASURES" USING btree ((properties->>'year_code'));
