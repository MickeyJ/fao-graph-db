-- Create PRODUCES relationships from production_indices
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:PRODUCES {
        -- Relationship semantic properties
        measure: 'per_capita',
        element_code: '434',
        element: 'Gross per capita Production Index Number (2014-2016 = 100)',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'production_indices'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM production_indices row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;