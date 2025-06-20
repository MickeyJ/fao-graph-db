-- Create INVESTS relationships from investment_government_expenditure
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:INVESTS {
        -- Relationship semantic properties
        measure: 'agriculture_orientation_index',
        currency: 'local',
        element_code: '6197',
        element: 'SDG 2.a.1: Agriculture Orientation Index (AOI) for Government Expenditure',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'investment_government_expenditure'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM investment_government_expenditure row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;