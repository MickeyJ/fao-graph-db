-- yaml_relationship_migration.cypher.sql.jinja2
-- Get records to create EMITS relationships from emissions_agriculture_energy
SELECT 
  COUNT(*)
FROM emissions_agriculture_energy t
  JOIN elements ON t.element_code_id = elements.id
  JOIN flags ON t.flag_id = flags.id
WHERE t.area_code_id IS NOT NULL
  AND t.item_code_id IS NOT NULL
  AND t.value > 0
  AND t.value != 'NaN'
  AND t.value IS NOT NULL
 
  AND elements.element_code IN ('7225', '7230', '7273')
 
  AND flags.flag IN ('A', 'X', 'E')
  AND t.year >= 2020
