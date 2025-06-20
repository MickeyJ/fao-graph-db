-- Create PRODUCES relationships from production_crops_livestock
SELECT * FROM cypher('fao_graph', $
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:PRODUCES {
 
        year: row.year, 
        unit: row.unit, 
        value: row.value, 
        note: row.note}]->(target)
$) AS (result agtype)
FROM production_crops_livestock row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;