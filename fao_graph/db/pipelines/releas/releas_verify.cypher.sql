-- Verification queries for Releas nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Releas)
    RETURN count(n)
$$) as (count agtype);