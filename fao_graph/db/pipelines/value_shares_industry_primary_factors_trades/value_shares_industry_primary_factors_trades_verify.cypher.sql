-- Verification queries for TRADES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:TRADES]->()
    WHERE r.source_dataset = 'value_shares_industry_primary_factors'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:TRADES]->(t)
    WHERE r.source_dataset = 'value_shares_industry_primary_factors'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.industry_codes as industry_codes,
           r.industry as industry,
           r.industry_code as industry_code,
           r.flow_direction as flow_direction,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, industry_codes agtype, industry agtype, industry_code agtype, flow_direction agtype, year agtype, value agtype, unit agtype);