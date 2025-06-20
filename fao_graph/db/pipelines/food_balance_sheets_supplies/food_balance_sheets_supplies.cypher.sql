-- Create SUPPLIES relationships from food_balance_sheets
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:SUPPLIES {
        -- Dynamic properties from row
        element_code_id: row.element_code_id,
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'food_balance_sheets'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM food_balance_sheets row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (671, 674, 681, 684, 661, 664, 5072, 5131, 5142, 5170, 5301, 5527)
;