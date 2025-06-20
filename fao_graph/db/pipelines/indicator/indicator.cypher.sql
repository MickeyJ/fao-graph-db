-- Create Indicator nodes from indicators
SELECT * FROM cypher('fao_graph', $
    CREATE (n:Indicator {
        id: row.id,
        indicator_code: row.indicator_code,
        indicator: row.indicator,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM indicators row;