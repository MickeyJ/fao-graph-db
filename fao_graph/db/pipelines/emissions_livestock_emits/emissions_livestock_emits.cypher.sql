-- Create EMITS relationships from emissions_livestock
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
        source_dataset: 'emissions_livestock'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM emissions_livestock row
WHERE row.area_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
  AND row.element_code IN (72254, 72256, 72300, 72301, 72306, 72340, 72341, 72346, 72360, 723601, 723602, 72361, 723611, 723612, 72366, 72431, 72441)
;