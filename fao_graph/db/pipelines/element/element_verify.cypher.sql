-- Verification queries for Element nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Element)
    RETURN count(n)
$$) as (count agtype);