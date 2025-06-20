-- Verification queries for MEASURES relationships
SELECT count(*) FROM cypher('fao_graph', $$
    MATCH ()-[r:MEASURES]->()
    WHERE r.source_dataset = 'trade_crops_livestock_indicators'
    RETURN count(r)
$$) as (count agtype);

-- Sample relationships with properties
SELECT * FROM cypher('fao_graph', $$
    MATCH (s)-[r:MEASURES]->(t)
    WHERE r.source_dataset = 'trade_crops_livestock_indicators'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target,
           r.category as category,
           r.indicator_code as indicator_code,
           r.indicator as indicator,
           r.year as year,
           r.value as value,
           r.unit as unit
    LIMIT 10
$$) as (source agtype, relationship agtype, target agtype
, category agtype, indicator_code agtype, indicator agtype, year agtype, value agtype, unit agtype);