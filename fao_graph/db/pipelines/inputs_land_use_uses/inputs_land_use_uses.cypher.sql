-- Create USES relationships from inputs_land_use
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:USES {
        -- Relationship semantic properties
        resource: 'inputs',
        measure: 'value',
        element_code: '7278',
        element: 'Value of agricultural production (Int. $) per Area',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'inputs_land_use'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM inputs_land_use row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;