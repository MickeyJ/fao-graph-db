-- Create Flag nodes from flags
SELECT * FROM cypher('fao_graph', $
    CREATE (n:Flag {
        id: row.id,
        flag: row.flag,
        description: row.description,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM flags row;