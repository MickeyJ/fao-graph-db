-- Verification queries for Release nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Release)
    RETURN count(n)
$$) as (count agtype);