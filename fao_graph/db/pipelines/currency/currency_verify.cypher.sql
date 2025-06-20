-- Verification queries for Currency nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Currency)
    RETURN count(n)
$$) as (count agtype);