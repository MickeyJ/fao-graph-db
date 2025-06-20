-- Create INVESTS relationships from investment_country_investment_statistics_profile
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
 
        note: row.note,
        -- Metadata
        source_dataset: 'investment_country_investment_statistics_profile'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM investment_country_investment_statistics_profile row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;