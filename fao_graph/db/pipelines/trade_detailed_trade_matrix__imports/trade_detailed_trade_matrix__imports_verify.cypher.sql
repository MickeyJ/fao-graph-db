-- yaml_relationship_verify.cypher.sql.jinja2
-- Verification queries for IMPORTS relationships from trade_detailed_trade_matrix
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:IMPORTS]->()
    WHERE r.source_dataset = 'trade_detailed_trade_matrix'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties

-- Value distribution (if no year but has value)
SELECT * FROM cypher('fao_graph', $$
    MATCH ()-[r:IMPORTS]->()
    WHERE r.source_dataset = 'trade_detailed_trade_matrix'
    RETURN 
        min(r.value) as min_value,
        max(r.value) as max_value,
        avg(r.value) as avg_value,
        count(*) as count
$$) as (min_value agtype, max_value agtype, avg_value agtype, count agtype);
