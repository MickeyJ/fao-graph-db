-- Create MEASURES relationships from environment_cropland_nutrient_budget
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCode {id: row.area_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:MEASURES {
        -- Relationship semantic properties
        category: 'general',
        measure: 'other',
        element_code: '7292',
        element: 'Cropland potassium use efficiency',
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'environment_cropland_nutrient_budget'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM environment_cropland_nutrient_budget row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;