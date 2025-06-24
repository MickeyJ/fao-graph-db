-- yaml_node_verify.cypher.sql.jinja2
-- Verification queries for ReporterCountryCode nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:ReporterCountryCode)
    RETURN count(n)
$$) as (count agtype);

-- Sample nodes
SELECT * FROM cypher('fao_graph', $$
    MATCH (n:ReporterCountryCode)
    RETURN n.id, n.reporter_country_code, n.reporter_countries
    LIMIT 10
$$) as (id agtype, reporter_country_code agtype, reporter_countries agtype);