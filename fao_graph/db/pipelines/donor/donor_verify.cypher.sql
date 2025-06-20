-- Verification queries for Donor nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:Donor)
    RETURN count(n)
$$) as (count agtype);