-- yaml_node_verify.cypher.sql.jinja2
-- Verification queries for ItemCode nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:ItemCode)
    RETURN count(n)
$$) as (count agtype);

-- Sample nodes
SELECT * FROM cypher('fao_graph', $$
    MATCH (n:ItemCode)
    RETURN n.id, n.item    LIMIT 10
$$) as (id agtype, item agtype);