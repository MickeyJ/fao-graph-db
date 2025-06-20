-- Create Purpos nodes from purposes
SELECT * FROM cypher('fao_graph', $
    CREATE (n:Purpos {
        id: row.id,
        purpose_code: row.purpose_code,
        purpose: row.purpose,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM purposes row;