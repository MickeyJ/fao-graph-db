-- Verification queries for Source nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Source)
    RETURN count(n)
$$) as (count agtype);