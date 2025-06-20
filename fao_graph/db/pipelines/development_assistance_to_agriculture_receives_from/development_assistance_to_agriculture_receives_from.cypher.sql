-- Create RECEIVES_FROM relationships from development_assistance_to_agriculture
SELECT * FROM cypher('fao_graph', $
    MATCH (source:RecipientCountryCode {id: row.recipient_country_code_id})
    MATCH (target:Donor {id: row.donor_code_id})
    CREATE (source)-[r:RECEIVES_FROM {
 
        year: row.year, 
        unit: row.unit, 
        value: row.value, 
        note: row.note}]->(target)
$) AS (result agtype)
FROM development_assistance_to_agriculture row
WHERE row.recipient_country_code_id IS NOT NULL
  AND row.donor_code_id IS NOT NULL
  AND row.value > 0
;