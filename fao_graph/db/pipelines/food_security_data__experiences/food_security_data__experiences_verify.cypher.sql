-- yaml_relationship_verify.cypher.sql.jinja2
-- Verification queries for EXPERIENCES relationships from food_security_data
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:EXPERIENCES]->()
    WHERE r.source_dataset = 'food_security_data'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties

-- Just count by relationship (no year or value columns)
SELECT * FROM cypher('fao_graph', $$
    MATCH ()-[r:EXPERIENCES]->()
    WHERE r.source_dataset = 'food_security_data'
    RETURN count(*) as total_relationships
$$) as (total_relationships agtype);
