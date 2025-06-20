-- Create MEASURES relationships from investment_credit_agriculture
SELECT * FROM cypher('fao_graph', $
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
 
        year: row.year, 
        unit: row.unit, 
        value: row.value,}]->(target)
$) AS (result agtype)
FROM investment_credit_agriculture row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;