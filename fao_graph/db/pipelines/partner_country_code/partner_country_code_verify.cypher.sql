-- yaml_node_verify.cypher.sql.jinja2
-- Verification queries for PartnerCountryCode nodes
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH (n:PartnerCountryCode)
    RETURN count(n)
$$) as (count agtype);

-- Sample nodes
SELECT * FROM cypher('fao_graph', $$
    MATCH (n:PartnerCountryCode)
    RETURN n.id, n.partner_country_code, n.partner_countries
    LIMIT 10
$$) as (id agtype, partner_country_code agtype, partner_countries agtype);