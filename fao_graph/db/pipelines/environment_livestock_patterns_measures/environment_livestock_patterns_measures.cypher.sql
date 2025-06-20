-- Create MEASURES relationships from environment_livestock_patterns
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'general',
        measure: 'area',
        element_code: '7213',
        element: 'Livestock units per agricultural land area',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'environment_livestock_patterns'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM environment_livestock_patterns row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;