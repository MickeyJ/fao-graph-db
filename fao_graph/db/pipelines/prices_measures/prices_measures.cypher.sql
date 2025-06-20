-- Create MEASURES relationships from prices
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'price',
        price_type: 'producer',
        currency: 'local',
        element_code: '5539',
        element: 'Producer Price Index (2014-2016 = 100)',
        -- Data properties from row
 
        year: row.year,
 
        months_code: row.months_code,
 
        months: row.months,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'prices'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM prices row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;