-- Create TRADES relationships from forestry_trade_flows
SELECT * FROM cypher('fao_graph', $
    MATCH (source:ReporterCountryCode {id: row.reporter_country_code_id})
    MATCH (target:PartnerCountryCode {id: row.partner_country_code_id})
    CREATE (source)-[r:TRADES {
 
        year: row.year, 
        unit: row.unit, 
        value: row.value, 
        note: row.note}]->(target)
$) AS (result agtype)
FROM forestry_trade_flows row
WHERE row.reporter_country_code_id IS NOT NULL
  AND row.partner_country_code_id IS NOT NULL
  AND row.value > 0
;