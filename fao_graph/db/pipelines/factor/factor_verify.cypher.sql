-- Verification queries for Factor nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Factor)
    RETURN count(n)
$$) as (count agtype);