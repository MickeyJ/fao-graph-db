-- Create MEASURES relationships from investment_foreign_direct_investment
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'financial',
        flow_type: 'foreign_direct_investment',
        element_code: '6184',
        element: 'Value US$, 2015 prices',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'investment_foreign_direct_investment'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM investment_foreign_direct_investment row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;