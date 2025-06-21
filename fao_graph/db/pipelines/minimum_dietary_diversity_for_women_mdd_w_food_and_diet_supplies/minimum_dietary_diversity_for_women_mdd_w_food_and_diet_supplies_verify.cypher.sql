-- Verification queries for SUPPLIES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:SUPPLIES]->()
    WHERE r.source_dataset = 'minimum_dietary_diversity_for_women_mdd_w_food_and_diet'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:SUPPLIES]->(t)
    WHERE r.source_dataset = 'minimum_dietary_diversity_for_women_mdd_w_food_and_diet'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.element_codes as element_codes,
           r.element as element,
           r.element_code as element_code,
           r.elements as elements,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, element_codes agtype, element agtype, element_code agtype, elements agtype, year agtype, value agtype, unit agtype);