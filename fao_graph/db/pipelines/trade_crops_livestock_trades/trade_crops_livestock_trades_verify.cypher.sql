-- Verification queries for TRADES relationships
SELECT count(*) FROM cypher('fao_graph', $
    MATCH ()-[r:TRADES]->()
    WHERE r.source_dataset = 'trade_crops_livestock'
    RETURN count(r)
$) as (count agtype);

-- Sample relationships
SELECT * FROM cypher('fao_graph', $
    MATCH (s)-[r:TRADES]->(t)
    WHERE r.source_dataset = 'trade_crops_livestock'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target
, r.year as year, r.value as value, r.unit as unit    LIMIT 10
$) as (source agtype, relationship agtype, target agtype
, year agtype, value agtype, unit agtype);