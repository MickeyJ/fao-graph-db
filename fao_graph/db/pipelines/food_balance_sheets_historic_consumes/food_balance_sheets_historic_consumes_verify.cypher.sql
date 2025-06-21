-- Verification queries for CONSUMES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:CONSUMES]->()
    WHERE r.source_dataset = 'food_balance_sheets_historic'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:CONSUMES]->(t)
    WHERE r.source_dataset = 'food_balance_sheets_historic'
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