-- Create SUPPLIES relationships from sua_crops_livestock
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