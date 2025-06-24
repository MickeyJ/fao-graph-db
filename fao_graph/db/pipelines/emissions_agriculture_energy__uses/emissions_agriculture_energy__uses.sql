-- yaml_relationship_migration.cypher.sql.jinja2
-- Get records to create USES relationships from emissions_agriculture_energy
SELECT 
  t.*,
  elements.element_code,
  elements.element,
  flags.flag,
  flags.description as flag_description
FROM emissions_agriculture_energy t
  JOIN elements ON t.element_code_id = elements.id
  JOIN flags ON t.flag_id = flags.id
WHERE t.area_code_id IS NOT NULL
  AND t.item_code_id IS NOT NULL
  AND t.value > 0
  AND t.value != 'NaN'
  AND t.value IS NOT NULL
 
  AND elements.element_code = '72184'
 
  AND flags.flag IN ('A', 'X', 'E')
  AND t.year >= 2020
ORDER BY t.id
LIMIT :limit OFFSET :offset
