-- Find commodities with dramatic year-over-year changes
WITH production_changes AS (
  SELECT 
    ic.item,
    ac.area,
    pcl.year,
    pcl.value as current_production,
    LAG(pcl.value) OVER (PARTITION BY ic.item, ac.area ORDER BY pcl.year) as prev_production,
    f.flag
  FROM production_crops_livestock pcl
  JOIN item_codes ic ON ic.id = pcl.item_code_id
  JOIN area_codes ac ON ac.id = pcl.area_code_id
  JOIN elements ec ON ec.id = pcl.element_code_id
  LEFT JOIN flags f ON f.id = pcl.flag_id
  WHERE LOWER(ec.element) LIKE '%production%'
    AND pcl.year BETWEEN 2015 AND 2023
    AND pcl.value > 0
    AND f.flag IN ('A', 'X', 'E')
    AND LENGTH(ac.area_code_m49) = 3
)
SELECT 
  item,
  area,
  year,
  current_production,
  prev_production,
  ROUND(((current_production - prev_production) / NULLIF(prev_production, 0) * 100)::numeric, 2) as percent_change
FROM production_changes
WHERE prev_production > 0
  AND ABS(current_production - prev_production) / prev_production > 0.5  -- More than 50% change
ORDER BY ABS(ROUND(((current_production - prev_production) / NULLIF(prev_production, 0) * 100)::numeric, 2)) DESC
LIMIT 50;