-- Create MEASURES relationships from employment_indicators_agriculture
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:Indicator {id: row.indicator_code_id})
    CREATE (source)-[r:MEASURES {
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'employment_indicators_agriculture'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM employment_indicators_agriculture row
WHERE row.area_code_id IS NOT NULL
  AND row.indicator_code_id IS NOT NULL
  AND row.value > 0
;