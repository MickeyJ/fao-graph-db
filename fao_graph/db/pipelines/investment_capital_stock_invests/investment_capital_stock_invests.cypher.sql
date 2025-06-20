-- Create INVESTS relationships from investment_capital_stock
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:INVESTS {
        -- Dynamic properties from row
        element_code_id: row.element_code_id,
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'investment_capital_stock'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM investment_capital_stock row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (61391, 61392, 61393, 61394, 6110, 61120, 6159, 6184, 6193, 61940, 6224, 6225)
;