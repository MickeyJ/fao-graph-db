-- Verification queries for SHARES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:SHARES]->()
    WHERE r.source_dataset = 'fertilizers_detailed_trade_matrix'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:SHARES]->(t)
    WHERE r.source_dataset = 'fertilizers_detailed_trade_matrix'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.pattern as pattern,
           r.source_fk as source_fk,
           r.target_fk as target_fk,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, pattern agtype, source_fk agtype, target_fk agtype, year agtype, value agtype, unit agtype);