-- yaml_node_migration.cypher.sql.jinja2
-- Create PartnerCountryCode nodes from partner_country_codes
SELECT * FROM cypher('fao_graph', $$
    CREATE (n:PartnerCountryCode {
        id: row.id,
        partner_country_code: row.partner_country_code,
        partner_countries: row.partner_countries,
        partner_country_code_m49: row.partner_country_code_m49,
        source_dataset: row.source_dataset    })
    RETURN n
$$) AS (result agtype)
FROM partner_country_codes row;