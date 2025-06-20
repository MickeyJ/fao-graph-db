-- Create SHARES relationships from forestry_trade_flows
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:ReporterCountryCodes {id: row.reporter_country_code_id})
    MATCH (target:PartnerCountryCodes {id: row.partner_country_code_id})
    CREATE (source)-[r:SHARES {
        -- Dynamic properties from row
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'forestry_trade_flows'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM forestry_trade_flows row
WHERE row.reporter_country_code_id IS NOT NULL
  AND row.partner_country_code_id IS NOT NULL
  AND row.value > 0
;