-- Verification queries for PopulationAgeGroup nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:PopulationAgeGroup)
    RETURN count(n)
$$) as (count agtype);