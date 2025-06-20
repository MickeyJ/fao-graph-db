-- Create RecipientCountryCode nodes from recipient_country_codes
SELECT * FROM cypher('fao_graph', $
    CREATE (n:RecipientCountryCode {
        id: row.id,
        recipient_country_code: row.recipient_country_code,
        recipient_country: row.recipient_country,
        recipient_country_code_m49: row.recipient_country_code_m49,
        source_dataset: row.source_dataset,
    })   
$) AS (result agtype)
FROM recipient_country_codes row;