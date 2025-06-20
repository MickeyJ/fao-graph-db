-- Verification queries for Purpos nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Purpos)
    RETURN count(n)
$$) as (count agtype);