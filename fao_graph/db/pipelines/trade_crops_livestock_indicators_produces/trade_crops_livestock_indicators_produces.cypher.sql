-- Create PRODUCES relationships from trade_crops_livestock_indicators
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:PRODUCES {
        -- Relationship semantic properties
        measure: 'self_sufficiency',
        indicator_code: '502',
        indicator: 'Self-sufficiency ratio',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'trade_crops_livestock_indicators'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM trade_crops_livestock_indicators row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;