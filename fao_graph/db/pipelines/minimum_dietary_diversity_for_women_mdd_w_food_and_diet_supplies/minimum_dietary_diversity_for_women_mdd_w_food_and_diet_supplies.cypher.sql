-- Create SUPPLIES relationships from minimum_dietary_diversity_for_women_mdd_w_food_and_diet
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:Surveys {id: row.survey_code_id})
    MATCH (target:FoodGroups {id: row.food_group_code_id})
    CREATE (source)-[r:SUPPLIES {
        -- Dynamic properties from row
        -- element_codes: row.element_codes,
        -- element: row.element,
        -- element_code: row.element_code,
        -- elements: row.elements,
        element_code_id: row.element_code_id, 
        unit: row.unit, 
        value: row.value,        -- Metadata
        source_dataset: 'minimum_dietary_diversity_for_women_mdd_w_food_and_diet'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM minimum_dietary_diversity_for_women_mdd_w_food_and_diet row
WHERE row.survey_code_id IS NOT NULL
  AND row.food_group_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (6121)
;


