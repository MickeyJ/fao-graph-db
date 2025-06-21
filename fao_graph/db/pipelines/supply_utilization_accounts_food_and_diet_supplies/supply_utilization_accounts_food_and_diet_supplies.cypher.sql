-- Create SUPPLIES relationships from supply_utilization_accounts_food_and_diet
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:FoodGroups {id: row.food_group_code_id})
    CREATE (source)-[r:SUPPLIES {
        -- Dynamic properties from row
        -- indicator_codes: row.indicator_codes,
        -- indicator: row.indicator,
        -- indicator_code: row.indicator_code,
        -- indicators: row.indicators,
        -- nutrient_type: row.nutrient_type,
        indicator_code_id: row.indicator_code_id, 
        year: row.year, 
        unit: row.unit, 
        value: row.value, 
        note: row.note,        -- Metadata
        source_dataset: 'supply_utilization_accounts_food_and_diet'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM supply_utilization_accounts_food_and_diet row
WHERE row.area_code_id IS NOT NULL
  AND row.food_group_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (6123, 6128, 6206, 6209)
  AND row.indicator_code IN (4004, 4005, 4007, 4009, 4010, 4017, 4018, 4024, 4029, 4033, 4034, 4035, 4036, 4003, 4006, 4011, 4012, 4013, 4015, 4016, 4021, 4022, 4032, 4037, 4038)
;


