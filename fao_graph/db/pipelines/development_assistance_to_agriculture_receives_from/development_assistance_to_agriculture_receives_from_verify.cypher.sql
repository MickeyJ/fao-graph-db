-- Verification queries for RECEIVES_FROM relationships
SELECT count(*) FROM cypher('fao_graph', $
    MATCH ()-[r:RECEIVES_FROM]->()
    WHERE r.source_dataset = 'development_assistance_to_agriculture'
    RETURN count(r)
$) as (count agtype);

-- Sample relationships
SELECT * FROM cypher('fao_graph', $
    MATCH (s)-[r:RECEIVES_FROM]->(t)
    WHERE r.source_dataset = 'development_assistance_to_agriculture'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target
, r.year as year, r.value as value, r.unit as unit    LIMIT 10
$) as (source agtype, relationship agtype, target agtype
, year agtype, value agtype, unit agtype);