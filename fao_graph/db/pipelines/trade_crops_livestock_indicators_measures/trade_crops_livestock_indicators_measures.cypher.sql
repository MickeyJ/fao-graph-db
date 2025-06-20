-- Create MEASURES relationships from trade_crops_livestock_indicators
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'trade_indicator',
        indicator_code: '508',
        indicator: 'Export market concentration index',
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