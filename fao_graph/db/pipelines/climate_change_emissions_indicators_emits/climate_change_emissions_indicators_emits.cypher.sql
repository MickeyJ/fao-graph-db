-- Create EMITS relationships from climate_change_emissions_indicators
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:EMITS {
        -- Relationship semantic properties
        source: 'other',
        gas_type: 'unspecified',
        category: 'general',
        element_code: '72792',
        element: 'Emissions per area of agricultural land',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'climate_change_emissions_indicators'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM climate_change_emissions_indicators row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;