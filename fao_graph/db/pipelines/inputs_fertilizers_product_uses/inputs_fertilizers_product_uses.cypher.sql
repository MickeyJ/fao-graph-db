-- Create USES relationships from inputs_fertilizers_product
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:USES {
        -- Relationship semantic properties
        resource: 'fertilizer',
        measure: 'other',
        element_code: '5510',
        element: 'Production',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'inputs_fertilizers_product'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM inputs_fertilizers_product row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;