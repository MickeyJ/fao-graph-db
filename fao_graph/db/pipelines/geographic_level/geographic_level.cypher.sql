-- Create GeographicLevel nodes from geographic_levels
SELECT * FROM cypher('fao_graph', $
    CREATE (n:GeographicLevel {
        id: row.id,
        geographic_level_code: row.geographic_level_code,
        geographic_level: row.geographic_level,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM geographic_levels row;