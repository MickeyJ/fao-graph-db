-- Create TRADES relationships from sua_crops_livestock
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:TRADES {
        -- Relationship semantic properties
        flow: 'export',
        measure: 'quantity',
        element_code: '5910',
        element: 'Export quantity',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'sua_crops_livestock'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM sua_crops_livestock row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;