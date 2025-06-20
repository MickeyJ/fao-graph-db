-- Create TRADES relationships from trade_detailed_trade_matrix
SELECT * FROM cypher('fao_graph', $
    MATCH (source:ReporterCountryCode {id: row.reporter_country_code_id})
    MATCH (target:PartnerCountryCode {id: row.partner_country_code_id})
    CREATE (source)-[r:TRADES {
 
        year: row.year, 
        unit: row.unit, 
        value: row.value,}]->(target)
$) AS (result agtype)
FROM trade_detailed_trade_matrix row
WHERE row.reporter_country_code_id IS NOT NULL
  AND row.partner_country_code_id IS NOT NULL
  AND row.value > 0
;