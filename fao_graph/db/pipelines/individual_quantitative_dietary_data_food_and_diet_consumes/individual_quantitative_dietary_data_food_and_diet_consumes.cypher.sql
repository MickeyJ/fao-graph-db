-- Create CONSUMES relationships from individual_quantitative_dietary_data_food_and_diet
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:Surveys {id: row.survey_code_id})
    MATCH (target:GeographicLevels {id: row.geographic_level_code_id})
    CREATE (source)-[r:CONSUMES {
        -- Dynamic properties from row
        -- indicator_codes: row.indicator_codes,
        -- indicator: row.indicator,
        -- indicator_code: row.indicator_code,
        -- indicators: row.indicators,
        indicator_code_id: row.indicator_code_id, 
        unit: row.unit, 
        value: row.value, 
        note: row.note,        -- Metadata
        source_dataset: 'individual_quantitative_dietary_data_food_and_diet'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM individual_quantitative_dietary_data_food_and_diet row
WHERE row.survey_code_id IS NOT NULL
  AND row.geographic_level_code_id IS NOT NULL
  AND row.value > 0
  AND row.indicator_code IN (3321, 3329, 3331, 3332, 3334, 3335, 3336, 3337, 3338, 3339, 3341, 3342, 3320)
;


