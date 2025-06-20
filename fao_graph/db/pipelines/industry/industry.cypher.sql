-- Create Industry nodes from industries
SELECT * FROM cypher('fao_graph', $
    CREATE (n:Industry {
        id: row.id,
        industry_code: row.industry_code,
        industry: row.industry,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM industries row;