-- Verification queries for SUPPLIES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:SUPPLIES]->()
    WHERE r.source_dataset = 'sua_crops_livestock'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:SUPPLIES]->(t)
    WHERE r.source_dataset = 'sua_crops_livestock'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.nutrient as nutrient,
           r.measure as measure,
           r.unit as unit,
           r.element_code as element_code,
           r.element as element,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, nutrient agtype, measure agtype, unit agtype, element_code agtype, element agtype, year agtype, value agtype, unit agtype);