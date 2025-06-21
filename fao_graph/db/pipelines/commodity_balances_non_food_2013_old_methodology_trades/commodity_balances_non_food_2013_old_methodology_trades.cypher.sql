-- Create TRADES relationships from commodity_balances_non_food_2013_old_methodology
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:TRADES {
        -- Dynamic properties from row
        -- element_codes: row.element_codes,
        -- element: row.element,
        -- element_code: row.element_code,
        -- elements: row.elements,
        -- flow_direction: row.flow_direction,
        element_code_id: row.element_code_id, 
        year: row.year, 
        unit: row.unit, 
        value: row.value,        -- Metadata
        source_dataset: 'commodity_balances_non_food_2013_old_methodology'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM commodity_balances_non_food_2013_old_methodology row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (5610, 5910)
;


