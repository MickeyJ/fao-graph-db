-- Create EMITS relationships from emissions_agriculture_energy
SELECT * FROM cypher('fao_graph', $
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:EMITS {
 
        year: row.year, 
        unit: row.unit, 
        value: row.value,}]->(target)
$) AS (result agtype)
FROM emissions_agriculture_energy row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;