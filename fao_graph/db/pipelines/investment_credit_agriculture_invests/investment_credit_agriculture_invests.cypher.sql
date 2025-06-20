-- Create INVESTS relationships from investment_credit_agriculture
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:INVESTS {
        -- Relationship semantic properties
        measure: 'agriculture_orientation_index',
        currency: 'USD',
        element_code: '6193',
        element: 'Agriculture orientation index US$, 2015 prices',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'investment_credit_agriculture'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM investment_credit_agriculture row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;