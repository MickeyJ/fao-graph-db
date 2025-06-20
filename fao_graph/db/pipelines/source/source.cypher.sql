-- Create Source nodes from sources
SELECT * FROM cypher('fao_graph', $
    CREATE (n:Source {
        id: row.id,
        source_code: row.source_code,
        source: row.source,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM sources row;