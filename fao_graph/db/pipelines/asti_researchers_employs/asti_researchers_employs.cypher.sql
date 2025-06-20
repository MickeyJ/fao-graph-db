-- Create EMPLOYS relationships from asti_researchers
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:EMPLOYS {
        -- Relationship semantic properties
        role: 'worker',
        measure: 'other',
        element_code: '6086',
        element: 'Per 100,000 farmers',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'asti_researchers'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM asti_researchers row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;