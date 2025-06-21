-- yaml_node_indexes.sql.jinja2
-- Indexes for PartnerCountryCode nodes
CREATE INDEX IF NOT EXISTS idx_partner_country_codes_id
ON fao_graph."PartnerCountryCode" (id);


-- Compound index for node lookups
CREATE INDEX IF NOT EXISTS idx_partner_country_codes_properties
ON fao_graph."PartnerCountryCode" USING GIN (properties);