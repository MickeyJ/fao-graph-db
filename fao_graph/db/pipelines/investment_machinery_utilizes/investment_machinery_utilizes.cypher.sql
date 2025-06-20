-- Create UTILIZES relationships from investment_machinery
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:UTILIZES {
        -- Dynamic properties from row
        element_code_id: row.element_code_id,
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'investment_machinery'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM investment_machinery row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (5116)
;