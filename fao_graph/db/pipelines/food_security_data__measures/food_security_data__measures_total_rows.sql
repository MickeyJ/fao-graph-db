-- yaml_relationship_migration.cypher.sql.jinja2
-- Get records to create MEASURES relationships from food_security_data
SELECT 
  COUNT(*)
FROM food_security_data t
  JOIN elements ON t.element_code_id = elements.id
  JOIN flags ON t.flag_id = flags.id
WHERE t.area_code_id IS NOT NULL
  AND t.item_code_id IS NOT NULL
  AND t.value > 0
  AND t.value != 'NaN'
  AND t.value IS NOT NULL
 
  AND elements.element_code IN ('6123', '6128', '6126', '6125', '6132', '6121', '6173', '6124')
 
  AND flags.flag IN ('A', 'X', 'E')
