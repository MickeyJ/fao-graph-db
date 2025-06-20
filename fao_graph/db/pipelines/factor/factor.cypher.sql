-- Create Factor nodes from factors
SELECT * FROM cypher('fao_graph', $
    CREATE (n:Factor {
        id: row.id,
        factor_code: row.factor_code,
        factor: row.factor,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM factors row;