-- Create MEASURES relationships from forestry_pulp_paper_survey
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'general',
        measure: 'other',
        element_code: '5801',
        element: 'Market pulp Production',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
        -- Metadata
        source_dataset: 'forestry_pulp_paper_survey'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM forestry_pulp_paper_survey row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;