-- Create EMITS relationships from emissions_drained_organic_soils
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:EMITS {
        -- Relationship semantic properties
        source: 'organic_soils',
        gas_type: 'CO2',
        category: 'general',
        element_code: '7273',
        element: 'Emissions (CO2)',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'emissions_drained_organic_soils'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM emissions_drained_organic_soils row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;