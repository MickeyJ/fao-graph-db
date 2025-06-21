-- Create EMITS relationships from emissions_crops
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:EMITS {
        -- Dynamic properties from row
        -- element_codes: row.element_codes,
        -- element: row.element,
        -- element_code: row.element_code,
        -- elements: row.elements,
        -- gas_type: row.gas_type,
        element_code_id: row.element_code_id, 
        year: row.year, 
        unit: row.unit, 
        value: row.value, 
        note: row.note,        -- Metadata
        source_dataset: 'emissions_crops'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM emissions_crops row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (72255, 72257, 72302, 72303, 72307, 72342, 72343, 72362, 723631, 723632, 72430, 72440)
;


