-- Verification queries for EMPLOYS relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:EMPLOYS]->()
    WHERE r.source_dataset = 'asti_expenditures'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:EMPLOYS]->(t)
    WHERE r.source_dataset = 'asti_expenditures'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.role as role,
           r.measure as measure,
           r.element_code as element_code,
           r.element as element,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, role agtype, measure agtype, element_code agtype, element agtype, year agtype, value agtype, unit agtype);