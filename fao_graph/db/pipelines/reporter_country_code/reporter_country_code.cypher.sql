-- Create ReporterCountryCode nodes from reporter_country_codes
SELECT * FROM cypher('fao_graph', $
    CREATE (n:ReporterCountryCode {
        id: row.id,
        reporter_country_code: row.reporter_country_code,
        reporter_countries: row.reporter_countries,
        reporter_country_code_m49: row.reporter_country_code_m49,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM reporter_country_codes row;