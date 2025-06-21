-- yaml_node_migration.cypher.sql.jinja2
-- Create AreaCode nodes from area_codes
SELECT * FROM cypher('fao_graph', $$
    CREATE (n:AreaCode {
        id: row.id,
        area_code: row.area_code,
        area: row.area,
        area_code_m49: row.area_code_m49,
        source_dataset: row.source_dataset    })
    RETURN n
$$) AS (result agtype)
FROM area_codes row;