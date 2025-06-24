-- yaml_relationship_verify.cypher.sql.jinja2
-- Verification queries for EXPERIENCES relationships from food_security_data
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:EXPERIENCES]->()
    WHERE r.source_dataset = 'food_security_data'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties

-- Value distribution (if no year but has value)
SELECT * FROM cypher('fao_graph', $$
    MATCH ()-[r:EXPERIENCES]->()
    WHERE r.source_dataset = 'food_security_data'
    RETURN 
        min(r.value) as min_value,
        max(r.value) as max_value,
        avg(r.value) as avg_value,
        count(*) as count
$$) as (min_value agtype, max_value agtype, avg_value agtype, count agtype);
