-- Indexes for population_age_group nodes
CREATE INDEX IF NOT EXISTS idx_population_age_groups_population_age_group_code
ON fao.population_age_group USING btree ((properties->>'population_age_group_code'));

CREATE INDEX IF NOT EXISTS idx_population_age_groups_source_dataset  
ON fao.population_age_group USING btree ((properties->>'source_dataset'));

