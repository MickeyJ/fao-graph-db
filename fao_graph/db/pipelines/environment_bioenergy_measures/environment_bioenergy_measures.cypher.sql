-- Create MEASURES relationships from environment_bioenergy
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'general',
        measure: 'other',
        element_code: '5852',
        element: 'Energy production',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'environment_bioenergy'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM environment_bioenergy row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;