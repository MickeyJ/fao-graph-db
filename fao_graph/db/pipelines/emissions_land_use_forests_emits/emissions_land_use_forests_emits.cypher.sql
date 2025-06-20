-- Create EMITS relationships from emissions_land_use_forests
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:EMITS {
        -- Relationship semantic properties
        source: 'other',
        gas_type: 'CO2',
        category: 'general',
        element_code: '72332',
        element: 'Net emissions/removals (CO2) (Forest land)',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'emissions_land_use_forests'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM emissions_land_use_forests row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;