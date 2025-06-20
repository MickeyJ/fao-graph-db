-- Create PRODUCES relationships from production_crops_livestock
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:PRODUCES {
        -- Dynamic properties from row
        element_code_id: row.element_code_id,
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'production_crops_livestock'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM production_crops_livestock row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (5412, 5413, 5417, 5424, 5312, 5318, 5313, 5510, 5513, 5111, 5112, 5114, 5320, 5321)
;