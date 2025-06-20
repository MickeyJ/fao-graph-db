-- Create SUPPLIES relationships from food_balance_sheets_historic
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:SUPPLIES {
        -- Relationship semantic properties
        nutrient: 'fat',
        measure: 'quantity',
        unit: 'g/capita/day',
        element_code: '684',
        element: 'Fat supply quantity (g/capita/day)',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'food_balance_sheets_historic'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM food_balance_sheets_historic row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;