-- Verification queries for EXCHANGES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:EXCHANGES]->()
    WHERE r.source_dataset = 'exchange_rate'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:EXCHANGES]->(t)
    WHERE r.source_dataset = 'exchange_rate'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, year agtype, value agtype, unit agtype);