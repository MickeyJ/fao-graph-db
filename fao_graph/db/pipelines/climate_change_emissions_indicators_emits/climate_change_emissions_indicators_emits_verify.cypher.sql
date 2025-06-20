-- Verification queries for EMITS relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:EMITS]->()
    WHERE r.source_dataset = 'climate_change_emissions_indicators'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:EMITS]->(t)
    WHERE r.source_dataset = 'climate_change_emissions_indicators'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.source as source,
           r.gas_type as gas_type,
           r.category as category,
           r.element_code as element_code,
           r.element as element,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, source agtype, gas_type agtype, category agtype, element_code agtype, element agtype, year agtype, value agtype, unit agtype);