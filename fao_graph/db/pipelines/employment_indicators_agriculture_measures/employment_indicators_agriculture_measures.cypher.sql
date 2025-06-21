-- Create MEASURES relationships from employment_indicators_agriculture
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:Sources {id: row.source_code_id})
    CREATE (source)-[r:MEASURES {
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
        source_dataset: 'employment_indicators_agriculture'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM employment_indicators_agriculture row
WHERE row.area_code_id IS NOT NULL
  AND row.source_code_id IS NOT NULL
  AND row.value > 0
  AND row.indicator_code IN (21150, 21151, 21152, 21155, 21156, 21157, 21158, 21161, 21162, 21164, 21167, 21114, 21118, 21126, 21160, 21163, 21085)
;


