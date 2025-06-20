-- Verification queries for Industry nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Industry)
    RETURN count(n)
$$) as (count agtype);