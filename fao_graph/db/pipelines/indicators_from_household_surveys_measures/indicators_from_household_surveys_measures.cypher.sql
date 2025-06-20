-- Create MEASURES relationships from indicators_from_household_surveys
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:Survey {id: row.survey_code_id})
    MATCH (target:Indicator {id: row.indicator_code_id})
    CREATE (source)-[r:MEASURES {
        -- Data properties from row
 
        breakdown_variable_code: row.breakdown_variable_code,
 
        breakdown_variable: row.breakdown_variable,
 
        breadown_by_sex_of_the_household_head_code: row.breadown_by_sex_of_the_household_head_code,
 
        breadown_by_sex_of_the_household_head: row.breadown_by_sex_of_the_household_head,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'indicators_from_household_surveys'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM indicators_from_household_surveys row
WHERE row.survey_code_id IS NOT NULL
  AND row.indicator_code_id IS NOT NULL
  AND row.value > 0
;