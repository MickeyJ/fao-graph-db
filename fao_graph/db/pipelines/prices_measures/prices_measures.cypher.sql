-- Create MEASURES relationships from prices
SELECT * FROM cypher('fao_graph', $
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
 
        year: row.year, 
        months_code: row.months_code, 
        months: row.months, 
        unit: row.unit, 
        value: row.value,}]->(target)
$) AS (result agtype)
FROM prices row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;