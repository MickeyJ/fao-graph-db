-- yaml_relationship_migration.cypher.sql.jinja2
-- Get records to create PRODUCES relationships from food_balance_sheets
SELECT 
  t.*,
  elements.element_code,
  elements.element,
  flags.flag,
  flags.description
FROM food_balance_sheets t
  JOIN elements ON t.element_code_id = elements.id
  JOIN flags ON t.flag_id = flags.id
WHERE t.area_code_id IS NOT NULL
  AND t.item_code_id IS NOT NULL
  AND t.value > 0
  AND t.value != 'NaN'
  AND t.value IS NOT NULL
  AND t.year >= 2022
  AND elements.element_code IN ('5511', '5301')
  AND flags.flag IN ('A', 'X', 'E')
ORDER BY t.id
LIMIT :limit OFFSET :offset