-- Create MEASURES relationships from cost_affordability_healthy_diet_co_ahd
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'general',
        measure: 'value',
        element_code: '6226',
        element: 'Value',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'cost_affordability_healthy_diet_co_ahd'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM cost_affordability_healthy_diet_co_ahd row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;