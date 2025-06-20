-- Create TRADES relationships from trade_indices
SELECT * FROM cypher('fao_graph', $
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:TRADES {
 
        year: row.year, 
        unit: row.unit, 
        value: row.value,}]->(target)
$) AS (result agtype)
FROM trade_indices row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;