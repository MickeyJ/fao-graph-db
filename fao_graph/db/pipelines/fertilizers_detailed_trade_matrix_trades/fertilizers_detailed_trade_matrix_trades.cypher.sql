-- Create TRADES relationships from fertilizers_detailed_trade_matrix
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:ReporterCountryCode {id: row.reporter_country_code_id})
    MATCH (target:PartnerCountryCode {id: row.partner_country_code_id})
    CREATE (source)-[r:TRADES {
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'fertilizers_detailed_trade_matrix'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM fertilizers_detailed_trade_matrix row
WHERE row.reporter_country_code_id IS NOT NULL
  AND row.partner_country_code_id IS NOT NULL
  AND row.value > 0
;