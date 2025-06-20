-- Verification queries for USES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:USES]->()
    WHERE r.source_dataset = 'food_balance_sheets'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:USES]->(t)
    WHERE r.source_dataset = 'food_balance_sheets'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.resource as resource,
           r.purpose as purpose,
           r.element_code as element_code,
           r.element as element,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, resource agtype, purpose agtype, element_code agtype, element agtype, year agtype, value agtype, unit agtype);