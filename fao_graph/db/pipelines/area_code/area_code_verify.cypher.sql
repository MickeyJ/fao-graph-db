-- yaml_node_verify.cypher.sql.jinja2
-- Verification queries for AreaCode nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:AreaCode)
    RETURN count(n)
$$) as (count agtype);

-- Sample nodes
SELECT * FROM cypher('fao_graph', $$
    MATCH (n:AreaCode)
    RETURN n.id, n.area_code, n.area
    LIMIT 10
$$) as (id agtype, area_code agtype, area agtype);