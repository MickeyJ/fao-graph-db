-- Create MEASURES relationships from environment_land_cover
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'general',
        measure: 'area',
        element_code: '5013',
        element: 'Area from WorldCover',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'environment_land_cover'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM environment_land_cover row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;