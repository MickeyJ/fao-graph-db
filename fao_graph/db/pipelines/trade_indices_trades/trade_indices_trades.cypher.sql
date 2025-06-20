-- Create TRADES relationships from trade_indices
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:TRADES {
        -- Relationship semantic properties
        flow: 'export',
        measure: 'value',
        element_code: '95',
        element: 'Export Value Base Price',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'trade_indices'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM trade_indices row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;