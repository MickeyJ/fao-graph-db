-- Verification queries for INVESTS relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:INVESTS]->()
    WHERE r.source_dataset = 'investment_government_expenditure'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:INVESTS]->(t)
    WHERE r.source_dataset = 'investment_government_expenditure'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.element_codes as element_codes,
           r.element as element,
           r.element_code as element_code,
           r.elements as elements,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, element_codes agtype, element agtype, element_code agtype, elements agtype, year agtype, value agtype, unit agtype);