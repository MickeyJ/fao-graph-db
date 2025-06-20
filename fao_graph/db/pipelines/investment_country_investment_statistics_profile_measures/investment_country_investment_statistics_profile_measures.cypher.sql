-- Create MEASURES relationships from investment_country_investment_statistics_profile
SELECT * FROM cypher('fao_graph', $
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
 
        year: row.year, 
        unit: row.unit, 
        value: row.value, 
        note: row.note}]->(target)
$) AS (result agtype)
FROM investment_country_investment_statistics_profile row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;