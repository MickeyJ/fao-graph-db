-- Verification queries for GeographicLevel nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:GeographicLevel)
    RETURN count(n)
$$) as (count agtype);