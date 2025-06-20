-- Create TRADES relationships from trade_crops_livestock
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:TRADES {
        -- Relationship semantic properties
        flow: 'export',
        content_type: 'nutrient',
        nutrient: 'vitamin_c',
        measure: 'content',
        element_code: '66028',
        element: 'Vitamin C content of exports (mg/capita/day)',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'trade_crops_livestock'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM trade_crops_livestock row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;