-- Create CONSUMES relationships from household_consumption_and_expenditure_surveys_food_and_diet
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:Surveys {id: row.survey_code_id})
    MATCH (target:GeographicLevels {id: row.geographic_level_code_id})
    CREATE (source)-[r:CONSUMES {
        -- Dynamic properties from row
        indicator_code_id: row.indicator_code_id,
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'household_consumption_and_expenditure_surveys_food_and_diet'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM household_consumption_and_expenditure_surveys_food_and_diet row
WHERE row.survey_code_id IS NOT NULL
  AND row.geographic_level_code_id IS NOT NULL
  AND row.value > 0
  AND row.indicator_code IN (3302, 3303, 3304, 3305, 3306, 3307, 3308, 3309, 3310, 3311, 3312, 3313, 3314, 3315, 3316, 3317, 3318, 3319, 3300)
;