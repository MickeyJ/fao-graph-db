-- Create PRODUCES relationships from food_balance_sheets
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:PRODUCES {
        -- Relationship semantic properties
        measure: 'quantity',
        element_code: '5511',
        element: 'Production',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'food_balance_sheets'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM food_balance_sheets row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;