-- Verification queries for ItemCode nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:ItemCode)
    RETURN count(n)
$$) as (count agtype);