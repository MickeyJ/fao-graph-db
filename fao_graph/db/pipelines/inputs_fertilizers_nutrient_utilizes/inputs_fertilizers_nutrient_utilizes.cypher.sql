-- Create UTILIZES relationships from inputs_fertilizers_nutrient
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:UTILIZES {
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
        source_dataset: 'inputs_fertilizers_nutrient'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM inputs_fertilizers_nutrient row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (5159, 5157, 5172, 5173, 5510)
;


