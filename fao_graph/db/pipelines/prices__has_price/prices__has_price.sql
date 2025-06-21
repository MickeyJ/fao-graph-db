-- yaml_relationship_migration.cypher.sql.jinja2
-- Get records to create HAS_PRICE relationships from prices
SELECT 
    t.*,
    elements.element_code,
    elements.element,
    flags.flag,
    flags.description
FROM prices t
  JOIN elements ON t.element_code_id = elements.id
  JOIN flags ON t.flag_id = flags.id
WHERE t.area_code_id IS NOT NULL
  AND t.item_code_id IS NOT NULL
  AND t.value > 0
  AND elements.element_code IN ('5530', '5532')
  AND flags.flag IN ('A', 'X')
ORDER BY t.id
LIMIT :limit OFFSET :offset