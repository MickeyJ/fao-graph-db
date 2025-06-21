-- Create TRADES relationships from value_shares_industry_primary_factors
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:AreaCodes {id: row.area_code_id})
    MATCH (target:FoodValues {id: row.food_value_code_id})
    CREATE (source)-[r:TRADES {
        -- Dynamic properties from row
        -- industry_codes: row.industry_codes,
        -- industry: row.industry,
        -- industry_code: row.industry_code,
        -- industries: row.industries,
        -- flow_direction: row.flow_direction,
        factor_code_id: row.factor_code_id, 
        year: row.year, 
        unit: row.unit, 
        value: row.value,        -- Metadata
        source_dataset: 'value_shares_industry_primary_factors'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM value_shares_industry_primary_factors row
WHERE row.area_code_id IS NOT NULL
  AND row.food_value_code_id IS NOT NULL
  AND row.value > 0
  AND row.factor_code IN (22125)
;


