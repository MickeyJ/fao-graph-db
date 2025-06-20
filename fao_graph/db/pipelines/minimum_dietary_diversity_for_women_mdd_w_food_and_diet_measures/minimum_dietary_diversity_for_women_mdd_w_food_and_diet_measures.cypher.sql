-- Create MEASURES relationships from minimum_dietary_diversity_for_women_mdd_w_food_and_diet
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:Survey {id: row.survey_code_id})
    MATCH (target:FoodGroup {id: row.food_group_code_id})
    CREATE (source)-[r:MEASURES {
        -- Data properties from row
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'minimum_dietary_diversity_for_women_mdd_w_food_and_diet'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM minimum_dietary_diversity_for_women_mdd_w_food_and_diet row
WHERE row.survey_code_id IS NOT NULL
  AND row.food_group_code_id IS NOT NULL
  AND row.value > 0
;