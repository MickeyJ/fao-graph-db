-- Verification queries for TRADES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:TRADES]->()
    WHERE r.source_dataset = 'inputs_fertilizers_nutrient'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:TRADES]->(t)
    WHERE r.source_dataset = 'inputs_fertilizers_nutrient'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.flow as flow,
           r.commodity_type as commodity_type,
           r.element_code as element_code,
           r.element as element,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, flow agtype, commodity_type agtype, element_code agtype, element agtype, year agtype, value agtype, unit agtype);