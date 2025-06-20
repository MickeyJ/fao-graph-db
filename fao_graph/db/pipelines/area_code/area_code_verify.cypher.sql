-- Verification queries for AreaCode nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:AreaCode)
    RETURN count(n)
$$) as (count agtype);