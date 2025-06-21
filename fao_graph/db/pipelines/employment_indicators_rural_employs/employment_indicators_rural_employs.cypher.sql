-- Create EMPLOYS relationships from employment_indicators_rural
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:Sources {id: row.source_code_id})
    CREATE (source)-[r:EMPLOYS {
        -- Dynamic properties from row
        -- indicator_codes: row.indicator_codes,
        -- indicator: row.indicator,
        -- indicator_code: row.indicator_code,
        -- indicators: row.indicators,
        indicator_code_id: row.indicator_code_id, 
        year: row.year, 
        unit: row.unit, 
        value: row.value, 
        note: row.note,        -- Metadata
        source_dataset: 'employment_indicators_rural'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM employment_indicators_rural row
WHERE row.area_code_id IS NOT NULL
  AND row.source_code_id IS NOT NULL
  AND row.value > 0
  AND row.indicator_code IN (21116, 21139, 21069, 21087, 21092, 21094, 21095, 21096, 21098, 21101, 21103, 21104, 21105, 21108, 21109, 21072, 21117, 21122, 21123, 21124)
;


