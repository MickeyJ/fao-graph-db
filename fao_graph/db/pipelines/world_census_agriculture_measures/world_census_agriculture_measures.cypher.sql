-- Create MEASURES relationships from world_census_agriculture
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'general',
        measure: 'other',
        element_code: '62021',
        element: 'Percent of total persons (household members)',
        -- Data properties from row
 
        wca_round_code: row.wca_round_code,
 
        wca_round: row.wca_round,
 
        census_year_code: row.census_year_code,
 
        census_year: row.census_year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'world_census_agriculture'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM world_census_agriculture row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;