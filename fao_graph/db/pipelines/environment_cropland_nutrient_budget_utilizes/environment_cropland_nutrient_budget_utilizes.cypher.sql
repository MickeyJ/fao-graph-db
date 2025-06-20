-- Create UTILIZES relationships from environment_cropland_nutrient_budget
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:ItemCodes {id: row.item_code_id})
    CREATE (source)-[r:UTILIZES {
        -- Dynamic properties from row
        element_code_id: row.element_code_id,
        year: row.year,
        value: row.value,
        unit: row.unit,
        -- Metadata
        source_dataset: 'environment_cropland_nutrient_budget'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM environment_cropland_nutrient_budget row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (7290, 7291, 7292)
;