-- Create INVESTS relationships from investment_credit_agriculture
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:INVESTS {
        -- Dynamic properties from row
        -- element_codes: row.element_codes,
        -- element: row.element,
        -- element_code: row.element_code,
        -- elements: row.elements,
        element_code_id: row.element_code_id, 
        year: row.year, 
        unit: row.unit, 
        value: row.value,        -- Metadata
        source_dataset: 'investment_credit_agriculture'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM investment_credit_agriculture row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (61133, 6110, 6184, 6193, 6224, 6225)
;


