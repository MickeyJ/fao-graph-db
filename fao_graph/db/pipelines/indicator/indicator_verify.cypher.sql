-- Verification queries for Indicator nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Indicator)
    RETURN count(n)
$$) as (count agtype);