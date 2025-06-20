-- Create TRADES relationships from inputs_pesticides_trade
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:TRADES {
        -- Relationship semantic properties
        flow: 'export',
        measure: 'value',
        element_code: '5922',
        element: 'Export value',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'inputs_pesticides_trade'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM inputs_pesticides_trade row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;