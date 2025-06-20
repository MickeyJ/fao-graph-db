-- Verification queries for RECEIVES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:RECEIVES]->()
    WHERE r.source_dataset = 'food_aid_shipments_wfp'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:RECEIVES]->(t)
    WHERE r.source_dataset = 'food_aid_shipments_wfp'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, year agtype, value agtype, unit agtype);