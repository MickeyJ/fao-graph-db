-- Create PRODUCES relationships from forestry_pulp_paper_survey
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
        value: row.value,        -- Metadata
        source_dataset: 'forestry_pulp_paper_survey'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM forestry_pulp_paper_survey row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (5510, 5801)
;


