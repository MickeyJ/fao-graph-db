-- Verification queries for Sex nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Sex)
    RETURN count(n)
$$) as (count agtype);