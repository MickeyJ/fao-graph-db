-- yaml_relationship_migration.cypher.sql.jinja2
-- Get records to create MEASURES relationships from food_security_data
SELECT 
  t.*,
  elements.element_code,
  elements.element,
  flags.flag,
  flags.description
FROM food_security_data t
  JOIN elements ON t.element_code_id = elements.id
  JOIN flags ON t.flag_id = flags.id
WHERE t.area_code_id IS NOT NULL
  AND t.item_code_id IS NOT NULL
  AND t.value > 0
  AND elements.element_code IN ('210011', '210012', '210013', '210041')
  AND flags.flag IN ('A', 'X', 'E')
ORDER BY t.id
LIMIT :limit OFFSET :offset