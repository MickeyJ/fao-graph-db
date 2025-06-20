-- Verification queries for MEASURES relationships
SELECT count(*) FROM cypher('fao_graph', $
    MATCH ()-[r:MEASURES]->()
    WHERE r.source_dataset = 'investment_capital_stock'
    RETURN count(r)
$) as (count agtype);

-- Sample relationships
SELECT * FROM cypher('fao_graph', $
    MATCH (s)-[r:MEASURES]->(t)
    WHERE r.source_dataset = 'investment_capital_stock'
    RETURN s.name as source, 
           type(r) as relationship, 
           t.name as target
, r.year as year, r.value as value, r.unit as unit    LIMIT 10
$) as (source agtype, relationship agtype, target agtype
, year agtype, value agtype, unit agtype);