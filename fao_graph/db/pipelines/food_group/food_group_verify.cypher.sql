-- Verification queries for FoodGroup nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:FoodGroup)
    RETURN count(n)
$$) as (count agtype);