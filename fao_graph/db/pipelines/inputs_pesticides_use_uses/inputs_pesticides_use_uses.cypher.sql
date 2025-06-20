-- Create USES relationships from inputs_pesticides_use
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:USES {
        -- Relationship semantic properties
        resource: 'inputs',
        measure: 'value',
        element_code: '5173',
        element: 'Use per value of agricultural production',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'inputs_pesticides_use'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM inputs_pesticides_use row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;