-- Create TRADES relationships from inputs_fertilizers_nutrient
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:TRADES {
        -- Relationship semantic properties
        flow: 'export',
        commodity_type: 'agricultural_inputs',
        element_code: '5910',
        element: 'Export quantity',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'inputs_fertilizers_nutrient'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM inputs_fertilizers_nutrient row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;