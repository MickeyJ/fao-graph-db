-- Verification queries for PRODUCES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:PRODUCES]->()
    WHERE r.source_dataset = 'food_balance_sheets'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:PRODUCES]->(t)
    WHERE r.source_dataset = 'food_balance_sheets'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.measure as measure,
           r.element_code as element_code,
           r.element as element,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, measure agtype, element_code agtype, element agtype, year agtype, value agtype, unit agtype);