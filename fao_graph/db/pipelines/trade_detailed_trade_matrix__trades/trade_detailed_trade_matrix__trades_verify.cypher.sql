- yaml_relationship_verify.cypher.sql.jinja2
-- Verification queries for TRADES relationships from trade_detailed_trade_matrix
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:TRADES]->()
    WHERE r.source_dataset = 'trade_detailed_trade_matrix'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:TRADES]->(t)
    WHERE r.source_dataset = 'trade_detailed_trade_matrix'
    RETURN 
        s.reporter_country_code as source,
        t.partner_country_code as target,
        r.year as year,
        r.value as value,
        r.unit as unit
    LIMIT 10
$$) as (source agtype, target agtype, year agtype, value agtype, unit agtype);

-- Group by year (only if table has year column)
SELECT * FROM cypher('fao_graph', $$
    MATCH ()-[r:TRADES]->()
    WHERE r.source_dataset = 'trade_detailed_trade_matrix'
    RETURN r.year as year, count(*) as count
    ORDER BY year DESC
    LIMIT 10
$$) as (year agtype, count agtype);
