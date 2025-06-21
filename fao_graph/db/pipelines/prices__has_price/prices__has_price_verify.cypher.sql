- yaml_relationship_verify.cypher.sql.jinja2
-- Verification queries for HAS_PRICE relationships from prices
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:HAS_PRICE]->()
    WHERE r.source_dataset = 'prices'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:HAS_PRICE]->(t)
    WHERE r.source_dataset = 'prices'
    RETURN 
        s.area_code as source,
        t.item_code as target,
        r.year as year,
        r.months as months,
        r.value as value,
        r.unit as unit
    LIMIT 10
$$) as (source agtype, target agtype, year agtype, months agtype, value agtype, unit agtype);

-- Group by year (only if table has year column)
SELECT * FROM cypher('fao_graph', $$
    MATCH ()-[r:HAS_PRICE]->()
    WHERE r.source_dataset = 'prices'
    RETURN r.year as year, count(*) as count
    ORDER BY year DESC
    LIMIT 10
$$) as (year agtype, count agtype);
