-- Indexes for survey nodes
CREATE INDEX IF NOT EXISTS idx_surveys_survey_code
ON fao.survey USING btree ((properties->>'survey_code'));

CREATE INDEX IF NOT EXISTS idx_surveys_source_dataset  
ON fao.survey USING btree ((properties->>'source_dataset'));

