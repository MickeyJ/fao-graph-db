-- yaml_relationship_migration.cypher.sql.jinja2
-- Get records to create TRADES relationships from trade_detailed_trade_matrix
SELECT 
  t.*,
  item_codes.item_code,
  item_codes.item,
  elements.element_code,
  elements.element,
  flags.flag,
  flags.description
FROM trade_detailed_trade_matrix t
  JOIN item_codes ON t.item_code_id = item_codes.id
  JOIN elements ON t.element_code_id = elements.id
  JOIN flags ON t.flag_id = flags.id
WHERE t.reporter_country_code_id IS NOT NULL
  AND t.partner_country_code_id IS NOT NULL
  AND t.value > 0
  AND t.value != 'NaN'
  AND t.value IS NOT NULL
  AND t.year >= 2022
  AND elements.element_code IN ('5910', '5922', '5610', '5622')
  AND flags.flag IN ('A')
ORDER BY t.id
LIMIT :limit OFFSET :offset