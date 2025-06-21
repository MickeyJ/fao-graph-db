-- Create PRODUCES relationships from prices
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
        months_code: row.months_code, 
        months: row.months, 
        unit: row.unit, 
        value: row.value,        -- Metadata
        source_dataset: 'prices'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM prices row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (5530, 5531, 5532, 5539)
;


