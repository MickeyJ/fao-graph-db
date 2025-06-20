-- Create SUPPLIES relationships from food_balance_sheets_historic
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
        source_dataset: 'food_balance_sheets_historic'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM food_balance_sheets_historic row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (674, 684, 664, 5074, 5131, 5142, 5301, 5527)
;