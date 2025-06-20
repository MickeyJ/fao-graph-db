-- Create EMPLOYS relationships from asti_expenditures
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:EMPLOYS {
        -- Relationship semantic properties
        role: 'worker',
        measure: 'other',
        element_code: '6084',
        element: 'Spending, total (constant 2011 prices)',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'asti_expenditures'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM asti_expenditures row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;