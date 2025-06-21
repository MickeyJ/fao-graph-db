-- Create MEASURES relationships from world_census_agriculture
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Dynamic properties from row
        -- element_codes: row.element_codes,
        -- element: row.element,
        -- element_code: row.element_code,
        -- elements: row.elements,
        element_code_id: row.element_code_id, 
        wca_round_code: row.wca_round_code, 
        wca_round: row.wca_round, 
        census_year_code: row.census_year_code, 
        census_year: row.census_year, 
        unit: row.unit, 
        value: row.value, 
        note: row.note,        -- Metadata
        source_dataset: 'world_census_agriculture'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM world_census_agriculture row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (5018, 50190, 50191, 6200, 5017, 6201, 62020)
;


