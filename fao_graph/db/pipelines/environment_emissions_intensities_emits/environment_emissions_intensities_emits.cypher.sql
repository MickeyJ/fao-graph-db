-- Create EMITS relationships from environment_emissions_intensities
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
        source_dataset: 'environment_emissions_intensities'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM environment_emissions_intensities row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (723113, 71761)
;


