-- Create TRADES relationships from inputs_fertilizers_archive
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:TRADES {
        -- Relationship semantic properties
        flow: 'export',
        commodity_type: 'agricultural_inputs',
        element_code: '5910',
        element: 'Export Quantity',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'inputs_fertilizers_archive'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM inputs_fertilizers_archive row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;