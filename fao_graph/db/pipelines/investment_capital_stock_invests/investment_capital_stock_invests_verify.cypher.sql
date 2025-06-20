-- Verification queries for INVESTS relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:INVESTS]->()
    WHERE r.source_dataset = 'investment_capital_stock'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:INVESTS]->(t)
    WHERE r.source_dataset = 'investment_capital_stock'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.measure as measure,
           r.currency as currency,
           r.element_code as element_code,
           r.element as element,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, measure agtype, currency agtype, element_code agtype, element agtype, year agtype, value agtype, unit agtype);