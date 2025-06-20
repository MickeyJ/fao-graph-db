-- Verification queries for TRADES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:TRADES]->()
    WHERE r.source_dataset = 'commodity_balances_non_food_2010'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:TRADES]->(t)
    WHERE r.source_dataset = 'commodity_balances_non_food_2010'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.element_codes as element_codes,
           r.element as element,
           r.element_code as element_code,
           r.flow_direction as flow_direction,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, element_codes agtype, element agtype, element_code agtype, flow_direction agtype, year agtype, value agtype, unit agtype);