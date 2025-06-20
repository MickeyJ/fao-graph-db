-- Create EMITS relationships from environment_emissions_intensities
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:EMITS {
        -- Relationship semantic properties
        source: 'other',
        gas_type: 'CO2',
        category: 'general',
        element_code: '723113',
        element: 'Emissions (CO2eq) (AR5)',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'environment_emissions_intensities'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM environment_emissions_intensities row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;