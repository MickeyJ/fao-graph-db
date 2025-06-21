-- Create SHARES relationships from fertilizers_detailed_trade_matrix
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:ReporterCountryCodes {id: row.reporter_country_code_id})
    MATCH (target:PartnerCountryCodes {id: row.partner_country_code_id})
    CREATE (source)-[r:SHARES {
        -- Dynamic properties from row
        -- pattern: row.pattern,
        -- source_fk: row.source_fk,
        -- target_fk: row.target_fk,
 
        year: row.year, 
        unit: row.unit, 
        value: row.value,        -- Metadata
        source_dataset: 'fertilizers_detailed_trade_matrix'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM fertilizers_detailed_trade_matrix row
WHERE row.reporter_country_code_id IS NOT NULL
  AND row.partner_country_code_id IS NOT NULL
  AND row.value > 0
;


