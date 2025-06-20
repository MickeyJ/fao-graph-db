-- Create MEASURES relationships from minimum_dietary_diversity_for_women_mdd_w_food_and_diet
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:Surveys {id: row.survey_code_id})
    MATCH (target:FoodGroups {id: row.food_group_code_id})
    CREATE (source)-[r:MEASURES {
        -- Dynamic properties from row
        indicator_code_id: row.indicator_code_id,
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'minimum_dietary_diversity_for_women_mdd_w_food_and_diet'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM minimum_dietary_diversity_for_women_mdd_w_food_and_diet row
WHERE row.survey_code_id IS NOT NULL
  AND row.food_group_code_id IS NOT NULL
  AND row.value > 0
  AND row.indicator_code IN (6211, 6212)
;