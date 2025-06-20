-- Create TRADES relationships from trade_crops_livestock
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:TRADES {
        -- Dynamic properties from row
        element_code_id: row.element_code_id,
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'trade_crops_livestock'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM trade_crops_livestock row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (5607, 5608, 5609, 5610, 5622, 5907, 5908, 5909, 5910, 5922, 50002, 50003, 50004, 50005, 50006, 50008, 50009, 50010, 50011, 50012, 50014, 50016, 50017, 50020, 50021, 50028, 66002, 66003, 66004, 66005, 66006, 66008, 66009, 66010, 66011, 66012, 66014, 66016, 66017, 66020, 66021, 66028)
;