-- Create MEASURES relationships from investment_capital_stock
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'financial',
        flow_type: 'general_investment',
        element_code: '6225',
        element: 'Value Standard Local Currency, 2015 prices',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'investment_capital_stock'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM investment_capital_stock row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;