-- Verification queries for PartnerCountryCode nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:PartnerCountryCode)
    RETURN count(n)
$$) as (count agtype);