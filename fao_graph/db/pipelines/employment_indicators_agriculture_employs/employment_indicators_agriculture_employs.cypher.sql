-- Create EMPLOYS relationships from employment_indicators_agriculture
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:Sources {id: row.source_code_id})
    CREATE (source)-[r:EMPLOYS {
        -- Dynamic properties from row
        indicator_code_id: row.indicator_code_id,
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'employment_indicators_agriculture'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM employment_indicators_agriculture row
WHERE row.area_code_id IS NOT NULL
  AND row.source_code_id IS NOT NULL
  AND row.value > 0
  AND row.indicator_code IN (21110, 21066, 21086, 21088, 21089, 21090, 21091, 21093, 21097, 21100, 21107, 21111, 21144)
;