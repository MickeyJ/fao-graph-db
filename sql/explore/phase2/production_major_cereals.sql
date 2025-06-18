-- Explore grain and cereal production patterns
SELECT 
  ic.item,
  ac.area,
  pcl.year,
  pcl.value as production,
  pcl.unit,
  RANK() OVER (PARTITION BY pcl.year ORDER BY pcl.value DESC) as global_rank
FROM production_crops_livestock pcl
JOIN item_codes ic ON ic.id = pcl.item_code_id
JOIN area_codes ac ON ac.id = pcl.area_code_id
JOIN elements ec ON ec.id = pcl.element_code_id
LEFT JOIN flags f ON f.id = pcl.flag_id
WHERE (LOWER(ic.item) LIKE '%wheat%' 
   OR LOWER(ic.item) LIKE '%rice%' 
   OR LOWER(ic.item) LIKE '%maize%'
   OR LOWER(ic.item) LIKE '%corn%'
   OR LOWER(ic.item) LIKE '%barley%'
   OR LOWER(ic.item) LIKE '%sorghum%')
  AND LOWER(ec.element) LIKE '%production%'
  AND pcl.year >= 2020
  AND pcl.value > 0
  AND f.flag IN ('A', 'X', 'E')
  -- Exclude regional aggregates - they have codes starting with 5 or other special patterns
  AND ac.area_code NOT LIKE '5%'  -- Excludes all FAO regional aggregates
  AND ac.area_code NOT LIKE '%-trade'  -- Excludes trade aggregates
  AND ac.area NOT LIKE '%(excluding intra-trade)%'  -- Excludes trade-specific regions
ORDER BY pcl.year DESC, pcl.value DESC
LIMIT 100;