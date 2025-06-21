-- Create EMITS relationships from climate_change_emissions_indicators
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
        value: row.value,        -- Metadata
        source_dataset: 'climate_change_emissions_indicators'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM climate_change_emissions_indicators row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (7179, 726313, 7264, 7265, 7266, 7279, 72791, 72792)
;


