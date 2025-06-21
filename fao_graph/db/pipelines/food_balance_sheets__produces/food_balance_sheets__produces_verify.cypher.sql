- yaml_relationship_verify.cypher.sql.jinja2
-- Verification queries for PRODUCES relationships from food_balance_sheets
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:PRODUCES]->()
    WHERE r.source_dataset = 'food_balance_sheets'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:PRODUCES]->(t)
    WHERE r.source_dataset = 'food_balance_sheets'
    RETURN 
        s.area_code as source,
        t.item_code as target,
        r.year as year,
        r.value as value,
        r.unit as unit,
        r.note as note
    LIMIT 10
$$) as (source agtype, target agtype, year agtype, value agtype, unit agtype, note agtype);

-- Group by year (only if table has year column)
SELECT * FROM cypher('fao_graph', $$
    MATCH ()-[r:PRODUCES]->()
    WHERE r.source_dataset = 'food_balance_sheets'
    RETURN r.year as year, count(*) as count
    ORDER BY year DESC
    LIMIT 10
$$) as (year agtype, count agtype);
