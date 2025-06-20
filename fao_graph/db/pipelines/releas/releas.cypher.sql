-- Create Releas nodes from releases
SELECT * FROM cypher('fao_graph', $
    CREATE (n:Releas {
        id: row.id,
        release_code: row.release_code,
        release: row.release,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM releases row;