-- Create EMITS relationships from emissions_totals
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:EMITS {
        -- Dynamic properties from row
        element_code_id: row.element_code_id,
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'emissions_totals'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM emissions_totals row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (724313, 724413, 717815, 7225, 7230, 723113, 7234, 7236, 7273)
;