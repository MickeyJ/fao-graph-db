-- Create Sex nodes from sexs
SELECT * FROM cypher('fao_graph', $
    CREATE (n:Sex {
        id: row.id,
        sex_code: row.sex_code,
        sex: row.sex,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM sexs row;