-- Create MEASURES relationships from commodity_balances_non_food_2013_old_methodology
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'general',
        measure: 'quantity',
        element_code: '5910',
        element: 'Export Quantity',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'commodity_balances_non_food_2013_old_methodology'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM commodity_balances_non_food_2013_old_methodology row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;