-- Create MEASURES relationships from prices_archive
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'price',
        price_type: 'producer',
        currency: 'local',
        element_code: '5530',
        element: 'Producer Price (LCU/tonne)',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'prices_archive'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM prices_archive row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;