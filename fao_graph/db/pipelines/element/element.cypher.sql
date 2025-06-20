-- Create Element nodes from elements
SELECT * FROM cypher('fao_graph', $
    CREATE (n:Element {
        id: row.id,
        element_code: row.element_code,
        element: row.element,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM elements row;