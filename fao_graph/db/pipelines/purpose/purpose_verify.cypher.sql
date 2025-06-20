-- Verification queries for Purpose nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Purpose)
    RETURN count(n)
$$) as (count agtype);