-- Create Survey nodes from surveys
SELECT * FROM cypher('fao_graph', $
    CREATE (n:Survey {
        id: row.id,
        survey_code: row.survey_code,
        survey: row.survey,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM surveys row;