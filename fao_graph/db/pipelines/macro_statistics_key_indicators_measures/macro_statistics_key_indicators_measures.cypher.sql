-- Create MEASURES relationships from macro_statistics_key_indicators
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Dynamic properties from row
        element_code_id: row.element_code_id,
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'macro_statistics_key_indicators'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM macro_statistics_key_indicators row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (6143, 61900, 6103, 61570, 6163, 61860, 6187, 61890, 6119, 61290, 61820, 6185, 6110, 6129, 61550, 61810, 6182, 6184, 6224, 6225)
;