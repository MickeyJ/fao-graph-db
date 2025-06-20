-- Create Currency nodes from currencies
SELECT * FROM cypher('fao_graph', $
    CREATE (n:Currency {
        id: row.id,
        iso_currency_code: row.iso_currency_code,
        currency: row.currency,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM currencies row;