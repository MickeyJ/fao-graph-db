-- Create EMITS relationships from emissions_livestock
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:EMITS {
        -- Relationship semantic properties
        source: 'livestock',
        gas_type: 'CH4',
        category: 'total',
        element_code: '72441',
        element: 'Livestock total (Emissions CH4)',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'emissions_livestock'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM emissions_livestock row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;