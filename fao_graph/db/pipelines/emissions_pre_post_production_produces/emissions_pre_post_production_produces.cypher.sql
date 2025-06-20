-- Create PRODUCES relationships from emissions_pre_post_production
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:PRODUCES {
        -- Relationship semantic properties
        measure: 'other',
        element_code: '7273',
        element: 'Emissions (CO2)',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'emissions_pre_post_production'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM emissions_pre_post_production row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;