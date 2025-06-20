-- Create EMITS relationships from emissions_crops
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:EMITS {
        -- Relationship semantic properties
        source: 'crops',
        gas_type: 'unspecified',
        category: 'general',
        element_code: '7245',
        element: 'Burning crop residues (Biomass burned, dry matter)',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'emissions_crops'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM emissions_crops row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;