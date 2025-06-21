-- Create PRODUCES relationships from sua_crops_livestock
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:PRODUCES {
        -- Dynamic properties from row
        -- element_codes: row.element_codes,
        -- element: row.element,
        -- element_code: row.element_code,
        -- elements: row.elements,
        element_code_id: row.element_code_id, 
        year: row.year, 
        unit: row.unit, 
        value: row.value, 
        note: row.note,        -- Metadata
        source_dataset: 'sua_crops_livestock'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM sua_crops_livestock row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (5510, 5113, 261, 271, 281, 5016, 5023, 5071, 5141, 5164, 5165, 5166, 5520, 5525, 664, 665, 674, 684, 511)
;


