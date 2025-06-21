-- Create SHARES relationships from development_assistance_to_agriculture
SELECT * FROM cypher('fao_graph', $$
    MATCH (source:Donors {id: row.donor_code_id})
    MATCH (target:RecipientCountryCodes {id: row.recipient_country_code_id})
    CREATE (source)-[r:SHARES {
        -- Dynamic properties from row
        -- pattern: row.pattern,
        -- source_fk: row.source_fk,
        -- target_fk: row.target_fk,
 
        year: row.year, 
        unit: row.unit, 
        value: row.value, 
        note: row.note,        -- Metadata
        source_dataset: 'development_assistance_to_agriculture'
    }]->(target)
    RETURN r
$$) AS (result agtype)
FROM development_assistance_to_agriculture row
WHERE row.donor_code_id IS NOT NULL
  AND row.recipient_country_code_id IS NOT NULL
  AND row.value > 0
;


