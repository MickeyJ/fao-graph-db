-- Verification queries for FoodValue nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:FoodValue)
    RETURN count(n)
$$) as (count agtype);