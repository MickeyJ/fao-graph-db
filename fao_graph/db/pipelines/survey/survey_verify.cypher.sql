-- Verification queries for Survey nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Survey)
    RETURN count(n)
$$) as (count agtype);