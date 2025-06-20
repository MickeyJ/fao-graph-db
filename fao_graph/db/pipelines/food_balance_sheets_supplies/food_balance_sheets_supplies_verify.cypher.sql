-- Verification queries for SUPPLIES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:SUPPLIES]->()
    WHERE r.source_dataset = 'food_balance_sheets'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:SUPPLIES]->(t)
    WHERE r.source_dataset = 'food_balance_sheets'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.element_codes as element_codes,
           r.element as element,
           r.element_code as element_code,
           r.nutrient_type as nutrient_type,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, element_codes agtype, element agtype, element_code agtype, nutrient_type agtype, year agtype, value agtype, unit agtype);