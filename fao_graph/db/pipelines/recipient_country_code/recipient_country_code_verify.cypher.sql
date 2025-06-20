-- Verification queries for RecipientCountryCode nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:RecipientCountryCode)
    RETURN count(n)
$$) as (count agtype);