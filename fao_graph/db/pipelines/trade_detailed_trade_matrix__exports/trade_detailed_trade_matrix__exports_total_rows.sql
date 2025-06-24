-- yaml_relationship_migration.cypher.sql.jinja2
-- Get records to create EXPORTS relationships from trade_detailed_trade_matrix
SELECT 
  COUNT(*)
FROM trade_detailed_trade_matrix t
  JOIN partner_country_codes ON t.partner_country_code_id = partner_country_codes.id
  JOIN elements ON t.element_code_id = elements.id
  JOIN flags ON t.flag_id = flags.id
WHERE t.reporter_country_code_id IS NOT NULL
  AND t.item_code_id IS NOT NULL
  AND t.value > 0
  AND t.value != 'NaN'
  AND t.value IS NOT NULL
 
  AND elements.element_code IN ('5910', '5922')
 
  AND flags.flag = 'A'
  AND t.year >= 2020
