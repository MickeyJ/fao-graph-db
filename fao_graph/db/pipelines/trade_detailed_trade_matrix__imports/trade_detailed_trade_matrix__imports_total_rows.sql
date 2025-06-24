-- yaml_relationship_migration.cypher.sql.jinja2
-- Get records to create IMPORTS relationships from trade_detailed_trade_matrix
SELECT 
  COUNT(*)
FROM trade_detailed_trade_matrix t
  JOIN reporter_country_codes ON t.reporter_country_code_id = reporter_country_codes.id
  JOIN elements ON t.element_code_id = elements.id
  JOIN flags ON t.flag_id = flags.id
WHERE t.item_code_id IS NOT NULL
  AND t.partner_country_code_id IS NOT NULL
  AND t.value > 0
  AND t.value != 'NaN'
  AND t.value IS NOT NULL
 
  AND elements.element_code IN ('5610', '5622')
 
  AND flags.flag = 'A'
  AND t.year >= 2020
