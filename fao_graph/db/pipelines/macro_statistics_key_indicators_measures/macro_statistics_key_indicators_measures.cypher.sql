-- Create MEASURES relationships from macro_statistics_key_indicators
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'general',
        measure: 'value',
        element_code: '6225',
        element: 'Value Standard Local Currency, 2015 prices',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'macro_statistics_key_indicators'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM macro_statistics_key_indicators row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;