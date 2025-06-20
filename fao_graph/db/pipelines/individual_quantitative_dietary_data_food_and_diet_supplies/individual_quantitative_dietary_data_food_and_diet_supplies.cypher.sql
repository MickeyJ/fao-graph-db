-- Create SUPPLIES relationships from individual_quantitative_dietary_data_food_and_diet
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:Surveys {id: row.survey_code_id})
    MATCH (target:GeographicLevels {id: row.geographic_level_code_id})
    CREATE (source)-[r:SUPPLIES {
        -- Dynamic properties from row
        element_code_id: row.element_code_id,
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'individual_quantitative_dietary_data_food_and_diet'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM individual_quantitative_dietary_data_food_and_diet row
WHERE row.survey_code_id IS NOT NULL
  AND row.geographic_level_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (6120, 6121, 6123, 6128, 6206, 6209)
;