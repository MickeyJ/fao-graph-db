-- Verification queries for CONSUMES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:CONSUMES]->()
    WHERE r.source_dataset = 'individual_quantitative_dietary_data_food_and_diet'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:CONSUMES]->(t)
    WHERE r.source_dataset = 'individual_quantitative_dietary_data_food_and_diet'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.indicator_codes as indicator_codes,
           r.indicator as indicator,
           r.indicator_code as indicator_code,
           r.indicators as indicators,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, indicator_codes agtype, indicator agtype, indicator_code agtype, indicators agtype, year agtype, value agtype, unit agtype);