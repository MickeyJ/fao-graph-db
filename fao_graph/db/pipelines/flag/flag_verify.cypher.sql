-- Verification queries for Flag nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Flag)
    RETURN count(n)
$$) as (count agtype);