-- Create EXCHANGES relationships from exchange_rate
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:Currency {id: row.iso_currency_code_id})
    CREATE (source)-[r:EXCHANGES {
        -- Data properties from row
 
        year: row.year,
 
        months_code: row.months_code,
 
        months: row.months,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'exchange_rate'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM exchange_rate row
WHERE row.area_code_id IS NOT NULL
  AND row.iso_currency_code_id IS NOT NULL
  AND row.value > 0
;