-- Create PRODUCES relationships from value_of_production
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:PRODUCES {
        -- Relationship semantic properties
        measure: 'value',
        element_code: '58',
        element: 'Gross Production Value (constant 2014-2016 thousand US$)',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'value_of_production'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM value_of_production row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;