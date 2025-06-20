-- Verification queries for ReporterCountryCode nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:ReporterCountryCode)
    RETURN count(n)
$$) as (count agtype);