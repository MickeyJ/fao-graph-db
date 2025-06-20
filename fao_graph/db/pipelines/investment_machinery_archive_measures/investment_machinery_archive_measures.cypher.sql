-- Create MEASURES relationships from investment_machinery_archive
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'financial',
        flow_type: 'general_investment',
        element_code: '5922',
        element: 'Export Value',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'investment_machinery_archive'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM investment_machinery_archive row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;