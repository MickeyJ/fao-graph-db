-- Create RECEIVES relationships from development_assistance_to_agriculture
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:RecipientCountryCode {id: row.recipient_country_code_id})
    MATCH (target:ItemCode {id: row.item_code_id})
    CREATE (source)-[r:RECEIVES {
        -- Data properties from row
 
        year: row.year,
 
        unit: row.unit,
 
        value: row.value,
 
        note: row.note,
        -- Metadata
        source_dataset: 'development_assistance_to_agriculture'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM development_assistance_to_agriculture row
WHERE row.recipient_country_code_id IS NOT NULL
  AND row.item_code_id IS NOT NULL
  AND row.value > 0
;